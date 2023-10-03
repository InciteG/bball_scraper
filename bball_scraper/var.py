import calendar
from datetime import datetime

if datetime.today().month>=9:
    current_season_year = datetime.today().year+1
else:
    current_season_year = datetime.today().year
            
all_seasons = [str(i) for i in range(2014,current_season_year+1)] # historical player data

core_seasons = [str(i) for i in range(2018,current_season_year+1)] # rosters for build and testing period

injury_suffix = '/friv/injuries.fcgi'

url_tags = {
    #key value is based on table id value
    
    #league page attribute tags
    'schedule':['date_game','game_start_time','visitor_team_name','visitor_pts','home_team_name',
                    'home_pts','box_score_text','overtimes','attendance','arena_name']
    
    #team page attribute tags
    , 'roster': ['player','pos','height','weight','birth_date','years_experience']
    
    , 'injuries': ['player','team_name','date_update','note']
    
    #boxscore page attribute tags
    , 'game-basic':['player','mp','fg','fga','fg_pct','fg3','fg3a','fg3_pct','ft','fta','ft_pct','orb','drb','trb','ast','stl',
                    'blk','tov','pf','pts','plus_minus']
}

season_months = [i.lower() for i in list(calendar.month_name)[1:]]

team_codes = {
    'ATL': 'ATLANTA_HAWKS',
    'BOS': 'BOSTON_CELTICS',
    'BRK': 'BROOKLYN_NETS',
    'CHI': 'CHICAGO_BULLS',
    'CHO': 'CHARLOTTE_HORNETS',
    'CLE': 'CLEVELAND_CAVALIERS',
    'DAL': 'DALLAS_MAVERICKS',
    'DEN': 'DENVER_NUGGETS',
    'DET': 'DETROIT_PISTONS',
    'GSW': 'GOLDEN_STATE_WARRIORS',
    'HOU': 'HOUSTON_ROCKETS',
    'IND': 'INDIANA_PACERS',
    'LAC': 'LOS_ANGELES_CLIPPERS',
    'LAL': 'LOS_ANGELES_LAKERS',
    'MEM': 'MEMPHIS_GRIZZLIES',
    'MIA': 'MIAMI_HEAT',
    'MIL': 'MILWAUKEE_BUCKS',
    'MIN': 'MINNESOTA_TIMBERWOLVES',
    'NOP': 'NEW_ORLEANS_PELICANS',
    'NYK': 'NEW_YORK_KNICKS',
    'OKC': 'OKLAHOMA_CITY_THUNDER',
    'ORL': 'ORLANDO_MAGIC',
    'PHI': 'PHILADELPHIA_76ERS',
    'PHO': 'PHOENIX_SUNS',
    'POR': 'PORTLAND_TRAIL_BLAZERS',
    'SAC': 'SACRAMENTO_KINGS',
    'SAS': 'SAN_ANTONIO_SPURS',
    'TOR': 'TORONTO_RAPTORS',
    'UTA': 'UTAH_JAZZ',
    'WAS': 'WASHINGTON_WIZARDS'}


all_team_codes = {
    'ATL': 'ATLANTA_HAWKS',
    'BOS': 'BOSTON_CELTICS',
    'BRK': 'BROOKLYN_NETS',
    'CHI': 'CHICAGO_BULLS',
    'CHO': 'CHARLOTTE_HORNETS',
    'CLE': 'CLEVELAND_CAVALIERS',
    'DAL': 'DALLAS_MAVERICKS',
    'DEN': 'DENVER_NUGGETS',
    'DET': 'DETROIT_PISTONS',
    'GSW': 'GOLDEN_STATE_WARRIORS',
    'HOU': 'HOUSTON_ROCKETS',
    'IND': 'INDIANA_PACERS',
    'LAC': 'LOS_ANGELES_CLIPPERS',
    'LAL': 'LOS_ANGELES_LAKERS',
    'MEM': 'MEMPHIS_GRIZZLIES',
    'MIA': 'MIAMI_HEAT',
    'MIL': 'MILWAUKEE_BUCKS',
    'MIN': 'MINNESOTA_TIMBERWOLVES',
    'NOP': 'NEW_ORLEANS_PELICANS',
    'NYK': 'NEW_YORK_KNICKS',
    'OKC': 'OKLAHOMA_CITY_THUNDER',
    'ORL': 'ORLANDO_MAGIC',
    'PHI': 'PHILADELPHIA_76ERS',
    'PHO': 'PHOENIX_SUNS',
    'POR': 'PORTLAND_TRAIL_BLAZERS',
    'SAC': 'SACRAMENTO_KINGS',
    'SAS': 'SAN_ANTONIO_SPURS',
    'TOR': 'TORONTO_RAPTORS',
    'UTA': 'UTAH_JAZZ',
    'WAS': 'WASHINGTON_WIZARDS',

    # DEPRECATED TEAMS
    'NJN': 'NEW_JERSEY_NETS',
    'NOH': 'NEW_ORLEANS_HORNETS',
    'NOK': 'NEW_ORLEANS_OKLAHOMA_CITY_HORNETS',
    'CHA': 'CHARLOTTE_BOBCATS',
    'CHH': 'CHARLOTTE_HORNETS',
    'SEA': 'SEATTLE_SUPERSONICS',
    'VAN': 'VANCOUVER_GRIZZLIES',
}
