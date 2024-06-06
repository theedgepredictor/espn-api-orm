from espn_api_orm.consts import ESPNSportTypes
from espn_api_orm.season.api import ESPNSeasonAPI

def example_get_season():
    sport_string = 'basketball'
    league_string = 'mens-college-basketball'
    print('yo')

    sport = ESPNSportTypes(sport_string)
    season_api = ESPNSeasonAPI(sport, league_string, 2023)
    print(season_api.get_season().__dict__)

if __name__ == "__main__":
    example_get_season()