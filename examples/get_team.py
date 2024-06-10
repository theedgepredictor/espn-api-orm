
from espn_api_orm.season.api import ESPNSeasonAPI
from espn_api_orm.team.api import ESPNTeamAPI

def example_get_team():

    sport = 'football'
    league = 'nfl'
    season = 2022

    season_api = ESPNSeasonAPI(sport, league, season)
    team_ids = season_api.get_team_ids()

    team_api = ESPNTeamAPI(sport, league, season, team_ids[0])
    print(team_api.get_team().__dict__)

if __name__ == "__main__":
    example_get_team()