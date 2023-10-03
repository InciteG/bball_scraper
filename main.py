from bball_scraper.var import all_seasons, team_codes, url_tags
from bball_scraper.main import pull_data

from datetime import datetime
from bs4 import BeautifulSoup as bs4
import pandas as pd
import prefect
from prefect import task, Flow




class setup_db:
    
    def __init__(self,data_store_path='data/',output_format='csv'):

        
        self.roster_filename = 'team_rosters.csv'
        self.league_filename = 'league_schedule.csv'
        self.boxscores_filename ='boxscores.csv'
        
        self.data_store_path=data_store_path
        self.output_format = output_format
        
        if datetime.today().month>=9:
            self.current_season = datetime.today().year+1
        else:
            self.current_season = datetime.today().year
        
    @Flow
    def setup_historical(self):
        setup_team_rosters()
        setup_league_schedule()
        setup_boxscores()
        update_injuries()
    @Flow   
    def run_update(self):
        update_injuries()
        most_recent_team_roster()
        most_recent_league_schedule()
        most_recent_boxscores()
    
    def __output(self,df,filename):
        if self.output_format=='csv':
            df.to_csv(f'{self.data_store_path}{filename}',  index=False) ##output to csv, replace with dynamodb load function later
        else:
            print('Output format not accepted at this time')
    
    def setup_team_rosters(self):
        big_df = pd.DataFrame()
        for year in all_seasons:
            for team in team_codes.keys():
            df_year = team_roster(year)
            big_df.append(df_year)      
        self.__output(big_df,self.roster_filename)
            
    def most_recent_team_roster(self):
        
        big_df = team_roster(self.current_season)        
        self.__output(big_df,self.roster_filename)
          
    def team_roster(self,year):
        html_id='all_roster'
        df_append = pd.DataFrame()
        col_names = url_tags[html_id] + ['page']
        for key,value in team_codes.items():
            try:
                url = url_build.team(key,year)
                response = requests.get(url,allow_redirects=False)
                time.sleep(3)
                soup = bs4(response.content, 'html.parser')
                row_list = get_tables(soup,html_id)
                df = pd.DataFrame(data=row_list, columns=data_stat_list)
                df['team']=key
                df['year']=year
                df_append=df_append.append(df)
                print(f'{year},{key} Query Complete')
            except:
                print(f'{year},{key} Query Fail')
        return df_append
    
    def get_injury_data(self):
        response = self.injury()
        soup = bs4(response.content, 'html.parser')
        rows = get_tables(soup, 'all_injuries')
        col_names = url_tags['all_injuries'] + ['page','player_code']
        df =pd.DataFrame(data=rows,columns=col_names)
        return df
    
    def update_injuries(self,filename='updated_injuries.csv'):
 
        big_df = self.get_injury_data()        
        self.__output(big_df,filename)

    def setup_league_schedule(self,filename='league_schedule.csv'):

        big_df = pd.DataFrame()
 
        for year in all_seasons:
            for month in season_months: 
                response = self.regular_season_schedule(year,month)
                if (response.status_code == 404):
                    print(f'{year},{month} not available')
                else:
                    soup = bs4(response.content, 'html.parser')
                    try:
                        row_list = get_tables(soup,'all_schedule')
                    except:
                        continue

                    df = pd.DataFrame(data=row_list, columns=col_names)
                    df['year']=year
                    big_df=big_df.append(df)
                    print(f'{year},{month} complete')


            if year=='2020':
                response = self.regular_season_schedule(year,'october-2019')
                soup = bs4(response.content, 'html.parser')
                row_list = get_tables(soup,'all_schedule')
                df = pd.DataFrame(data=row_list, columns=col_names)
                df['year']=year
                big_df=big_df.append(df)
                print(f'{year}, october-2019 complete')

                response = self.regular_season_schedule(year,'october-2020')
                soup = bs4(response.content, 'html.parser')
                row_list = get_tables(soup,'all_schedule')
                df = pd.DataFrame(data=row_list, columns=col_names)
                df['year']=year
                big_df=big_df.append(df) 

                print(f'{year},october-2020 complete')
            else:
                pass
        
        big_df['date_game']=pd.to_datetime(big_df['date_game'],format='%a, %b %d, %Y', errors='coerce')
        big_df['game_id']=big_df['box_score_page'].map(lambda x: x[11:23])
        
        big_df.sort_values(by='date_game',ascending=True, inplace=True)
        if self.output_format=='csv':
            big_df.to_csv(self.league_filename,  index=False) ##output to csv, replace with dynamodb load function later
        else:
            print('Output format not accepted at this time')
 
    def setup_boxscores(self, output_format='csv',filename='boxscores.csv'):
        self.boxscores_filename=filename
        schedule = pd.read_csv(self.league_filename)
        schedule['game_id']=schedule['box_score_page'].map(lambda x: x[11:23])
        
#         boxscores =  pd.read_csv(r'boxscores.csv')
#         remaining_games = schedule.loc[~schedule.game_id.isin(boxscores.game_id.unique())]
        big_df=pd.DataFrame()
        table_type='game-basic'
        col_names = ['game_id','game_type','team_code','player_code']+[i for i in url_tags[table_type]]+['play_status']

        for page_tag,game_id in zip(schedule.box_score_page.values,schedule.game_id.values):

            response = self.boxscores(page_tag)
            soup = bs4(response.content, 'html.parser')
            df_row_list = get_boxscores(soup,table_type,game_id)
            df = pd.DataFrame(data=df_row_list, columns=col_names)
            big_df =big_df.append(df)
            print(f'{game_id} complete')
            
        if output_format=='csv':
            big_df.to_csv(self.boxscores_filename,  index=False) ##output to csv, replace with dynamodb load function later
        else:
            print('Output format not accepted at this time')
        
    def resolve_missing_boxscores(self, output_format='csv',filename='boxscores.csv'):
        self.boxscores_filename=filename
        schedule = pd.read_csv(self.league_filename)
        schedule['game_id']=schedule['box_score_page'].map(lambda x: x[11:23])
        
        boxscores =  pd.read_csv(self.boxscores_filename)
        remaining_games = schedule.loc[~schedule.game_id.isin(boxscores.game_id.unique())]
        big_df=pd.DataFrame()
        table_type='game-basic'
        col_names = ['game_id','game_type','team_code','player_code']+[i for i in url_tags[table_type]]+['play_status']

        for page_tag,game_id in zip(remaining_games.box_score_page.values,remaining_games.game_id.values):

            response = self.boxscores(page_tag)
            soup = bs4(response.content, 'html.parser')
            df_row_list = get_boxscores(soup,table_type,game_id)
            df = pd.DataFrame(data=df_row_list, columns=col_names)
            big_df =big_df.append(df)
            print(f'{game_id} complete')
            
        complete_boxscores = boxscores.append(big_df)
        
        if output_format=='csv':
            complete_boxscores.to_csv(self.boxscores_filename,  index=False) ##output to csv, replace with dynamodb load function later
        else:
            print('Output format not accepted at this time')
      
