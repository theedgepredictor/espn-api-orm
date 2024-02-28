from espn_api_orm.consts import ESPNSportTypes
from espn_api_orm.generic.api import ESPNBaseAPI
from espn_api_orm.sport.api import ESPNSportAPI
from espn_api_orm.league.api import ESPNLeagueAPI
from espn_api_orm.season.api import ESPNSeasonAPI

base_api = ESPNBaseAPI()
single_test = False
sport_string ='basketball'
sport = ESPNSportTypes(sport_string)

league_string = 'mens-college-basketball'

sport_api = ESPNSportAPI(sport)
sport_obj = sport_api.get_sport()

league_api = ESPNLeagueAPI(sport, league_string)
league_obj = league_api.get_league()

seasons_list = [2024] if single_test else league_api.get_seasons(return_values=True)
seasons = []
valid_seasons = []
for season in seasons_list:
    season_api = ESPNSeasonAPI(sport, league_string, season)
    season_obj = season_api.get_season()
    if not season_obj.type.hasStandings:
        continue
    season_types = season_api.get_valid_types(return_values=True)
    seasons.append({'season': season_obj, 'types':season_types})
    valid_seasons.append(season)
print(seasons)

print(valid_seasons)
