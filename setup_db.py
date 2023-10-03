from bball_scraper.var import all_seasons, core_seasons, team_codes, url_tags, current_season_year, injury_suffix
from bball_scraper.main import pull_data

from datetime import datetime
from bs4 import BeautifulSoup as bs4
import pandas as pd
import prefect
from prefect import task, Flow

url_build = UrlBuilder()

class setup:
    
    def __init__(self, data_store_path='data/', output_format='csv'):
        self.roster_filename = 'team_rosters'
        self.schedule_filename = 'schedule'
        self.boxscores_filename ='boxscores'
        self.injury_filename = 'injuries'
        self.data_store_path= data_store_path
        self.output_format = output_format
        self.current_season = current_season_year
        
    def run_setup(self):
        setup_tables(table_type='injuries')
        setup_tables(table_type='roster')
        schedule_df = setup_tables(table_type='schedule')
        self.__boxscore_url_list = schedule_df.boxscore_url.values
        setup_tables(table_type='game-basic')
    
    def run_update(self):
        update_tables(table_type='injuries', run_type='update')
        update_tables(table_type='roster', run_type='update')
        schedule_df = update_tables(table_type='schedule', run_type='update')
        self.__boxscore_url_list = schedule_df.boxscore_url.values
        update_tables(table_type='game-basic', run_type='update')
    
    def setup_tables( 
    self,
    table_type: str,
    run_type: Optional['str']='setup'):
        """ This function defines the logic to loop through web pages to scrape. "setup" mode runs through all data from 2014 onwards. Other run_types will only load the most recent season into separate files.

        Parameters
        ----------

        table_type: str
            Table type code, See var.py url_tags.keys() for accepted values
        run_type: str
            Defines how to loop through webpages to scrape. 

        Returns
        -------
        Pandas dataframe with data from the specified table.
        """
        
        if run_type =='setup':
            season_list = core_seasons
            schedule_season_list = all_seasons
        else:
            season_list = [current_season_year]
            schedule_season_list = [current_season_year]
            self.roster_filename = f'team_rosters_{current_season_year}'
            self.schedule_filename = f'schedule_{current_season_year}'
            self.boxscores_filename =f'boxscores_{current_season_year}'
            
        
        outer_df_list = []
        if table_type=='injuries':
            df = pull_data(table_type=table_type, suffix=injury_suffix)
            outer_df_list.append(df)
        elif table_type == 'roster':  
            for season in core_seasons:
                for team in team_codes.keys():
                    df = pull_data(table_type=table_type, team=team,season=season)
                    outer_df_list.append(df)
        elif table_type == 'schedule':
            for season in schedule_season_list:
                for month in season_months:
                    try:
                        df = pull_data(table_type=table_type, month=month,season=season)
                        outer_df_list.append(df)
                    except:
                        print(f'{season} {month}')
                        pass
                
                #add covid related schedule month pages
                if season=='2020':
                    month_special = 'october-2019'
                    df = pull_data(table_type=table_type, month=month_special,season='2020')
                    outer_df_list.append(df)

                    month_special = 'october-2020'
                    df = pull_data(table_type=table_type, month=month_special,season='2020')
                    outer_df_list.append(df)
        elif table_type == 'game-basic':  
            for suffix in self.__boxscore_url_list:
                df = pull_data(table_type=table_type,suffix=suffix)
                outer_df_list.append(df)
    
        outer_df = pd.concat(outer_df_list)   
        self.__output(table_type,outer_df)
        return outer_df
    
    # private functions
    def __output(self,table_type,df):
        if table_type == 'injuries':
            filename = self.injury_filename
        elif table_type == 'roster':
            filename = self.roster_filename
        elif table_type == 'schedule':
            filename = self.schedule_filename
        elif table_type == 'game-basic':
            filename = self.boxscores_filename
        
        if self.output_format=='csv':
            df.to_csv(f'{self.data_store_path}{filename}.csv',  index=False)
        else:
            print('Output format not accepted at this time')

if __name__ == "__main__":
    setup.run_setup()
    