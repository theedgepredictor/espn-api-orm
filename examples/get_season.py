from espn_api_orm.consts import ESPNSportTypes
from espn_api_orm.generic.api import ESPNBaseAPI
from espn_api_orm.league.api import ESPNLeagueAPI
from espn_api_orm.season.api import ESPNSeasonAPI
from espn_api_orm.sport.api import ESPNSportAPI


def example_get_season():
    sport = 'football'
    league = 'nfl'
    season = 2022

    # Get all available sports
    base = ESPNBaseAPI()
    print(base.get_sports())

    # Get all available leagues for the given sport
    sport_api = ESPNSportAPI(sport)
    print(sport_api.get_sport())
    sport_api.get_leagues()

    # Get all available seasons for the given league
    league_api = ESPNLeagueAPI(sport, league)
    print(league_api.get_league())
    league_api.get_seasons()

    # Get all available teams for the given season
    season_api = ESPNSeasonAPI(sport, league, season)
    print(season_api.get_season().__dict__)

if __name__ == "__main__":
    example_get_season()