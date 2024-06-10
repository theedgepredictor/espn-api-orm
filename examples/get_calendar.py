from espn_api_orm.calendar.api import ESPNCalendarAPI
from espn_api_orm.consts import ESPNSportTypes
from espn_api_orm.generic.api import ESPNBaseAPI
from espn_api_orm.league.api import ESPNLeagueAPI
from espn_api_orm.season.api import ESPNSeasonAPI
from espn_api_orm.sport.api import ESPNSportAPI


def example_get_calendar():

    calendar = ESPNCalendarAPI('football', 'nfl', 2022)
    print(calendar.get_calendar())
    season_type_ids = calendar.get_valid_types()

    weeks_for_season_type_dict = {}
    groups_for_season_type_dict = {}
    for season_type_id in season_type_ids:
        weeks_for_season_type_dict[season_type_id] = calendar.get_weeks(season_type_id)
        groups_for_season_type_dict[season_type_id] = calendar.get_groups(season_type_id)
    print(weeks_for_season_type_dict)

    print('Calendar Sections:')
    print(calendar.get_calendar_sections(season_type_ids))

if __name__ == "__main__":
    example_get_calendar()