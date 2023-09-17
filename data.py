class OutputType():
    JSON = "JSON"
    CSV = "CSV"


class OutputWriteOption():
    WRITE = "w"
    CREATE_AND_WRITE = "w+"
    APPEND = "a"
    APPEND_AND_WRITE = "a+"


class Position():
    POINT_GUARD = "POINT GUARD"
    SHOOTING_GUARD = "SHOOTING GUARD"
    SMALL_FORWARD = "SMALL FORWARD"
    POWER_FORWARD = "POWER FORWARD"
    CENTER = "CENTER"
    FORWARD = "FORWARD"
    GUARD = "GUARD"


class PeriodType():
    QUARTER = "QUARTER"
    OVERTIME = "OVERTIME"


class League():
    NATIONAL_BASKETBALL_ASSOCIATION = "NATIONAL_BASKETBALL_ASSOCIATION"
    AMERICAN_BASKETBALL_ASSOCIATION = "AMERICAN_BASKETBALL_ASSOCIATION"
    BASKETBALL_ASSOCIATION_OF_AMERICA = "BASKETBALL_ASSOCIATION_OF_AMERICA"


class Conference():
    EASTERN = "EASTERN"
    WESTERN = "WESTERN"


class Division():
    ATLANTIC = "ATLANTIC"
    CENTRAL = "CENTRAL"
    MIDWEST = "MIDWEST"
    NORTHWEST = "NORTHWEST"
    PACIFIC = "PACIFIC"
    SOUTHEAST = "SOUTHEAST"
    SOUTHWEST = "SOUTHWEST"


# DIVISIONS_TO_CONFERENCES = {
#     Division.ATLANTIC: Conference.EASTERN,
#     Division.CENTRAL: Conference.EASTERN,
#     Division.SOUTHEAST: Conference.EASTERN,
#     Division.MIDWEST: Conference.WESTERN,
#     Division.PACIFIC: Conference.WESTERN,
#     Division.SOUTHWEST: Conference.WESTERN,
#     Division.NORTHWEST : Conference.WESTERN
# }
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


# TEAM_ABBREVIATIONS_TO_TEAM = {
#     'ATL': Team.ATLANTA_HAWKS,
#     'BOS': Team.BOSTON_CELTICS,
#     'BRK': Team.BROOKLYN_NETS,
#     'CHI': Team.CHICAGO_BULLS,
#     'CHO': Team.CHARLOTTE_HORNETS,
#     'CLE': Team.CLEVELAND_CAVALIERS,
#     'DAL': Team.DALLAS_MAVERICKS,
#     'DEN': Team.DENVER_NUGGETS,
#     'DET': Team.DETROIT_PISTONS,
#     'GSW': Team.GOLDEN_STATE_WARRIORS,
#     'HOU': Team.HOUSTON_ROCKETS,
#     'IND': Team.INDIANA_PACERS,
#     'LAC': Team.LOS_ANGELES_CLIPPERS,
#     'LAL': Team.LOS_ANGELES_LAKERS,
#     'MEM': Team.MEMPHIS_GRIZZLIES,
#     'MIA': Team.MIAMI_HEAT,
#     'MIL': Team.MILWAUKEE_BUCKS,
#     'MIN': Team.MINNESOTA_TIMBERWOLVES,
#     'NOP': Team.NEW_ORLEANS_PELICANS,
#     'NYK': Team.NEW_YORK_KNICKS,
#     'OKC': Team.OKLAHOMA_CITY_THUNDER,
#     'ORL': Team.ORLANDO_MAGIC,
#     'PHI': Team.PHILADELPHIA_76ERS,
#     'PHO': Team.PHOENIX_SUNS,
#     'POR': Team.PORTLAND_TRAIL_BLAZERS,
#     'SAC': Team.SACRAMENTO_KINGS,
#     'SAS': Team.SAN_ANTONIO_SPURS,
#     'TOR': Team.TORONTO_RAPTORS,
#     'UTA': Team.UTAH_JAZZ,
#     'WAS': Team.WASHINGTON_WIZARDS,

#     # DEPRECATED TEAMS
#     'NJN': Team.NEW_JERSEY_NETS,
#     'NOH': Team.NEW_ORLEANS_HORNETS,
#     'NOK': Team.NEW_ORLEANS_OKLAHOMA_CITY_HORNETS,
#     'CHA': Team.CHARLOTTE_BOBCATS,
#     'CHH': Team.CHARLOTTE_HORNETS,
#     'SEA': Team.SEATTLE_SUPERSONICS,
#     'VAN': Team.VANCOUVER_GRIZZLIES,
# }

# TEAM_TO_TEAM_ABBREVIATION = {v: k for k, v in TEAM_ABBREVIATIONS_TO_TEAM.items()}
# TEAM_TO_TEAM_ABBREVIATION[Team.CHARLOTTE_HORNETS] = "CHO"

# TEAM_NAME_TO_TEAM = {
#     "ATLANTA HAWKS": Team.ATLANTA_HAWKS,
#     "BOSTON CELTICS": Team.BOSTON_CELTICS,
#     "BROOKLYN NETS": Team.BROOKLYN_NETS,
#     "CHARLOTTE HORNETS": Team.CHARLOTTE_HORNETS,
#     "CHICAGO BULLS": Team.CHICAGO_BULLS,
#     "CLEVELAND CAVALIERS": Team.CLEVELAND_CAVALIERS,
#     "DALLAS MAVERICKS": Team.DALLAS_MAVERICKS,
#     "DENVER NUGGETS": Team.DENVER_NUGGETS,
#     "DETROIT PISTONS": Team.DETROIT_PISTONS,
#     "GOLDEN STATE WARRIORS": Team.GOLDEN_STATE_WARRIORS,
#     "HOUSTON ROCKETS": Team.HOUSTON_ROCKETS,
#     "INDIANA PACERS": Team.INDIANA_PACERS,
#     "LOS ANGELES CLIPPERS": Team.LOS_ANGELES_CLIPPERS,
#     "LOS ANGELES LAKERS": Team.LOS_ANGELES_LAKERS,
#     "MEMPHIS GRIZZLIES": Team.MEMPHIS_GRIZZLIES,
#     "MIAMI HEAT": Team.MIAMI_HEAT,
#     "MILWAUKEE BUCKS": Team.MILWAUKEE_BUCKS,
#     "MINNESOTA TIMBERWOLVES": Team.MINNESOTA_TIMBERWOLVES,
#     "NEW ORLEANS PELICANS": Team.NEW_ORLEANS_PELICANS,
#     "NEW YORK KNICKS": Team.NEW_YORK_KNICKS,
#     "OKLAHOMA CITY THUNDER": Team.OKLAHOMA_CITY_THUNDER,
#     "ORLANDO MAGIC": Team.ORLANDO_MAGIC,
#     "PHILADELPHIA 76ERS": Team.PHILADELPHIA_76ERS,
#     "PHOENIX SUNS": Team.PHOENIX_SUNS,
#     "PORTLAND TRAIL BLAZERS": Team.PORTLAND_TRAIL_BLAZERS,
#     "SACRAMENTO KINGS": Team.SACRAMENTO_KINGS,
#     "SAN ANTONIO SPURS": Team.SAN_ANTONIO_SPURS,
#     "TORONTO RAPTORS": Team.TORONTO_RAPTORS,
#     "UTAH JAZZ": Team.UTAH_JAZZ,
#     "WASHINGTON WIZARDS": Team.WASHINGTON_WIZARDS,

#     # DEPRECATED TEAMS
#     "CHARLOTTE BOBCATS": Team.CHARLOTTE_BOBCATS,
#     "NEW JERSEY NETS": Team.NEW_JERSEY_NETS,
#     "NEW ORLEANS HORNETS": Team.NEW_ORLEANS_HORNETS,
#     "NEW ORLEANS/OKLAHOMA CITY HORNETS": Team.NEW_ORLEANS_OKLAHOMA_CITY_HORNETS,
#     "SEATTLE SUPERSONICS": Team.SEATTLE_SUPERSONICS,
#     "VANCOUVER GRIZZLIES": Team.VANCOUVER_GRIZZLIES,
# }

# POSITION_ABBREVIATIONS_TO_POSITION = {
#     "PG": Position.POINT_GUARD,
#     "SG": Position.SHOOTING_GUARD,
#     "SF": Position.SMALL_FORWARD,
#     "PF": Position.POWER_FORWARD,
#     "C": Position.CENTER,
#     "F": Position.FORWARD,
#     "G": Position.GUARD,
# }


# LOCATION_ABBREVIATIONS_TO_POSITION = {
#     "": Location.HOME,
#     "@": Location.AWAY,
# }


# OUTCOME_ABBREVIATIONS_TO_OUTCOME = {
#     "W": Outcome.WIN,
#     "L": Outcome.LOSS,
# }

# LEAGUE_ABBREVIATIONS_TO_LEAGUE = {
#     "NBA": League.NATIONAL_BASKETBALL_ASSOCIATION,
#     "ABA": League.AMERICAN_BASKETBALL_ASSOCIATION,
#     "BAA": League.BASKETBALL_ASSOCIATION_OF_AMERICA,
# }


# class TeamTotal:
#     def __init__(self, team_abbreviation, totals):
#         self.team_abbreviation = team_abbreviation
#         self.totals = totals

#     @property
#     def minutes_played(self):
#         return self.totals.minutes_played

#     @property
#     def made_field_goals(self):
#         return self.totals.made_field_goals

#     @property
#     def attempted_field_goals(self):
#         return self.totals.attempted_field_goals

#     @property
#     def made_three_point_field_goals(self):
#         return self.totals.made_three_point_field_goals

#     @property
#     def attempted_three_point_field_goals(self):
#         return self.totals.attempted_three_point_field_goals

#     @property
#     def made_free_throws(self):
#         return self.totals.made_free_throws

#     @property
#     def attempted_free_throws(self):
#         return self.totals.attempted_free_throws

#     @property
#     def offensive_rebounds(self):
#         return self.totals.offensive_rebounds

#     @property
#     def defensive_rebounds(self):
#         return self.totals.defensive_rebounds

#     @property
#     def assists(self):
#         return self.totals.assists

#     @property
#     def steals(self):
#         return self.totals.steals

#     @property
#     def blocks(self):
#         return self.totals.blocks

#     @property
#     def turnovers(self):
#         return self.totals.turnovers

#     @property
#     def personal_fouls(self):
#         return self.totals.personal_fouls

#     @property
#     def points(self):
#         return self.totals.points


# class PlayerData:
#     def __init__(self, name, resource_location, league_abbreviations):
#         self.name = name
#         self.resource_location = resource_location
#         self.league_abbreviations = set(league_abbreviations)