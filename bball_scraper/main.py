import requests
import time
import re
from bs4 import BeautifulSoup as bs
import bs4
import pandas as pd
from typing import Dict, Iterable, List, Optional, Set, Tuple, Union
from bball_scraper.checks import check_value, check_not_value
from bball_scraper.logging import get_logger
from prefect import task
from bball_scraper.var import url_tags, current_season_year, all_seasons, season_months, all_team_codes

log=get_logger(__name__)
    
def pull_data( 
    table_type: str, 
    team_code: Optional[str] = None,
    season: Optional[str] = None,
    month: Optional[str] = None,
    suffix: Optional[str] = None
):
    """ Function that encompasses:
    1. Querying the webpage
    2. Reading tables from webpage
    3. Updating tables with additional data from webpage
    
    Parameters
    ----------
    
    table_type: str
        Table type code, See var.py url_tags.keys() for accepted values
    team_code: str, optional
        Team code value used for querying team pages. Functionality is used to query for team rosters
    season: str, optional
        Year value expressed as a string. Used to query team pages or league schedule pages. E.g. 2023-2024 season would be "2024"
    month: str, optional
        Month value expressed as full name. (e.g. january) Value is used to query league schedule pages.
    suffix: str, optional
        General string value to attach any suffix desired to basketball reference base_url
        
    Returns
    -------
    Dataframe object with data based on argument specifications.
    """
    response = get_response(table_type=table_type,team_code=team_code,season=season,month=month,suffix=suffix)
    soup = bs(response.content, 'html.parser')
    df= parse_tables(soup,table_type)
    
    if team_code != None:
        df['team_code']=team_code
    if season != None:
        df['season']=season
    if (suffix != None) & (table_type=='game-basic'):
        df['game_id']=response.url[-17:-5]
    return df
        
def get_response( 
    table_type: str, 
    team_code: Optional[str] = None,
    season: Optional[str] = None,
    month: Optional[str] = None,
    suffix: Optional[str] = None
):
    """ Builds basketball reference URL based on inputs
    
    Parameters
    ----------
    
    table_type: str
        Table type code, See var.py url_tags.keys() for accepted values 
    team_code: str, optional
        Team code value used for querying team pages. Functionality is used to query for team rosters
    season: str, optional
        Year value expressed as a string. Used to query team pages or league schedule pages. E.g. 2023-2024 season would be "2024"
    month: str, optional
        Month value expressed as full name. (e.g. january) Value is used to query league schedule pages.
    suffix: str, optional
        General string value to attach any suffix desired to basketball reference base_url
    
    
    
    Returns
    -------
    Response object from requests package
    """
    base_url =  'https://www.basketball-reference.com'

    
    if table_type in ('injuries','game-basic'):
        check_not_value('suffix', suffix, [None])
        url= f'{base_url}{suffix}'
    elif table_type=='roster':
        check_value('team_code',team_code,list(all_team_codes.keys()))
        check_value('season',season,all_seasons)        
        url = f'{base_url}/teams/{team_code}/{season}.html'
    elif table_type=='schedule':
        check_value('season', season, all_seasons)
        check_value('month', month, season_months)  
        url = f'{base_url}/leagues/NBA_{season}_games-{month}.html'
    
    for n in range(3): #try 3 times
        response = requests.get(url, allow_redirects=False)
        time.sleep(3) #meet bbref rate limit of 20 hits per minute
        
        if response.status_code==200:
            log.info(f'Succcessful page response received from: {url}')
            break
        elif response.status_code == 429: #if too many requests, wait 1 hour
            log.info(f'Status code {response.status_code} found. Trying again in one hour. Try number: {n}')
            time.sleep(3600)
        elif response.status_code == 502: #bad gateway, try again in 5 minutes
            log.info(f'Status code {response.status_code} found. Trying again in five minutes. Try number: {n}')
            time.sleep(300)
        else: # else proceed
            log.debug(f'Status code {response.status_code} found. Try number: {n}')      
    
    return response

def parse_tables( 
    soup: bs4.BeautifulSoup, 
    table_type: str,
):
    """ This function defines the logic to find page elements that correspond to the desired data.
    
    Parameters
    ----------
    
    soup: bs4.Soup object
        Object contains page elements.
    table_type: str
        Table type code, See var.py url_tags.keys() for accepted values
    
    Returns
    -------
    Pandas dataframe with data from the specified table.
    """

    check_value('table_type',table_type,list(url_tags.keys()))
    
    tables = soup.find_all('table',attrs={'id':re.compile(table_type)})
    
    table_list = []
    
    count=0
    for table in tables:
        rows = table.find('tbody').find_all('tr',{'class':None}) #filter out subheaders
        
        if table_type=='game-basic':
            team=table['id'][4:7]
        for row in rows:
            try:
                row_dict = __parse_row(row,table_type)
                
                if table_type=='game-basic':
                    row_dict['team']=team
                
                table_list.append(row_dict)   
            except:
                pass
            
    df = pd.DataFrame(data=table_list)
    
    ## table_type specific updates to tables
    
    # get game type information if table_type is 'game-basic'
    if table_type =='game-basic':
        header = soup.find('h1').text
        if (re.search("Conference",header) is not None) | (re.search("Final",header) is not None):
            game_type='playoff'
        elif (re.search("Play-In",header) is not None):
            game_type='playin'
        else:
            game_type='regular'
        
        df['game_type']=game_type
    return df

def __parse_row(
    row: bs4.element.Tag , 
    table_type: str,
):
    """ This function defines the logic to parse a particular row within a table.
    
    Parameters
    ----------
    
    row: bs4.element.Tag object
        Beautiful Soup Tag object that contains individual data points 
    table_type: str
        Table type code, See var.py url_tags.keys() for accepted values   
    
    Returns
    -------
    Dictionary object with data from the specified row.
    """
    check_value('table_type',table_type,list(url_tags.keys()))
    try:
        row_dict = {stat:row.find(attrs={"data-stat": stat}).text for stat in url_tags[table_type]}
        if table_type=='game-basic':
            row_dict['play_status']='Played'
    except:
        if table_type =='game-basic':
            row_dict = {'player': row.find(attrs={"data-stat": 'player'}).text}
            for stat in url_tags[table_type][1:]:
                row_dict[stat]=0
            row_dict['play_status'] = row.find(attrs={"data-stat": 'reason'}).text

    
    #additional processing for data specific to certain tables
    if table_type in ('roster','injuries','game-basic'):
        player_url=row.find(attrs={"data-stat": 'player'}).find('a')['href']
        player_code = player_url[11:-5]
        row_dict['player_url']=player_url
        row_dict['player_code']=player_code #join key 
    elif table_type=='schedule':
        try:
            boxscore_url_tag=row.find(attrs={"data-stat": 'box_score_text'}).find('a')['href']
            row_dict['boxscore_url']=boxscore_url_tag
            row_dict['game_id']=boxscore_url_tag[-17:-5]
        except:
            row_dict['boxscore_url']=None
            row_dict['game_id']=None
    return row_dict

    