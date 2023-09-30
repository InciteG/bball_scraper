from bball_scraper.var import url_tags
import re
from bs4 import BeautifulSoup as bs4

# def get_roster(soup):
#     html_id = 'all_roster'
#     data_stat_list = url_tags[html_id]
#     df_row_list = []
#     for row in soup.find(id=html_id).find_all('tr')[1:]:
#         df_row = [row.find(attrs={"data-stat": stat}).text for stat in data_stat_list]
        
#         player_url_tag=row.find(attrs={"data-stat": 'player'}).find('a')['href']
#         df_row.append(player_url_tag)
#         df_row_list.append(df_row)
#     return df_row_list

def get_tables(soup, table_type):
    # supports roster tables and league schedule tables
    df_row_list = []
    
    table_rows = soup.find(id=table_type).find_all('tr')[1:]
    
    for row in table_rows:
        try:
            df_row = [row.find(attrs={"data-stat": stat}).text for stat in url_tags[table_type]]
        except:
            continue

        #conditions on table_type for extra information
        if table_type in ('all_roster','all_injuries'):
            player_url_tag=row.find(attrs={"data-stat": 'player'}).find('a')['href']
            player_code = player_url_tag[11:-5]
            df_row.append(player_url_tag)
            df_row.append(player_code)
        elif table_type=='all_schedule':
            boxscore_url_tag=row.find(attrs={"data-stat": 'box_score_text'}).find('a')['href']
            df_row.append(boxscore_url_tag)
        else:
            pass
        df_row_list.append(df_row)
        
    return df_row_list

def get_boxscores(soup, table_type,game_id):
    #find game type
    header = soup.find('h1').text

    if (re.search("Conference",header) is not None) | (re.search("Final",header) is not None):
        game_type='playoff'
    elif (re.search("Play-In",header) is not None):
        game_type='playin'
    else:
        game_type='regular'
    
    df_row_list = []
    boxscore_tables = soup.find_all('table',attrs={'id':re.compile(r'game-basic')})
    teams = soup.find('div',attrs={'class':'scorebox'}).find_all('strong')
    for table,team in zip(boxscore_tables,teams):
        table_rows = table.find('tbody').find_all('tr',{'class':None})
        team_code = team.a['href'][7:10] #get team_code


        for row in table_rows:
            player_code=row.find(attrs={"data-stat": 'player'})['data-append-csv'] #get player_code
            df_row = [game_id,game_type,team_code,player_code]

            try:
                df_row_append = [row.find(attrs={"data-stat": stat}).text for stat in url_tags[table_type]]
                play_status = 'Played'

            except:
                try:                
                    df_row_append = [row.find(attrs={"data-stat": 'player'}).text] + [0 for i in range(len(url_tags[table_type])-1)]
                    play_status = row.find(attrs={"data-stat": 'reason'}).text
                except:
                    continue

            df_row_append.append(play_status)
            df_row = df_row+df_row_append
            df_row_list.append(df_row)
        
    return df_row_list
