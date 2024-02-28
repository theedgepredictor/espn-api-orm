from espn_api_orm.consts import ESPNSportTypes
from espn_api_orm.generic.api import ESPNBaseAPI
from espn_api_orm.sport.api import ESPNSportAPI
from espn_api_orm.league.api import ESPNLeagueAPI

base_api = ESPNBaseAPI()
single_test = False
sport_strings = ['basketball'] if single_test else base_api.get_sports(return_values=True)

sports = []
sport_types = []
for sport_string in sport_strings:
    sport = ESPNSportTypes(sport_string)
    sport_api = ESPNSportAPI(sport)
    sport_obj = sport_api.get_sport()
    league_strings = ['mens-college-basketball'] if single_test else sport_api.get_leagues(return_values=True)
    leagues = []
    for league_string in league_strings:
        sport_type = f"{sport_string}/{league_string}"
        league_api = ESPNLeagueAPI(sport, league_string)
        league_obj = league_api.get_league()
        leagues.append({'league_name': league_string, 'league': league_obj})
        sport_types.append(sport_type)
    sports.append({'sport_name': sport.value, 'sport': sport_obj, 'league_names': league_strings, 'leagues': leagues})
print(sport_types)

