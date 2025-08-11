# Copilot Instructions for espn-api-orm

## Background

`espn-api-orm` is a Python package that provides an ORM-like interface for interacting with ESPN's public API endpoints. It abstracts the complexity of direct API calls, allowing developers to work with sports data (NFL, NBA, MLB, etc.) using Python classes and methods. The project covers endpoints for teams, athletes, events, seasons, scoreboards, venues, and more, with a focus on NFL but extensible to other leagues.

## ESPN API Relationship Diagram

This diagram shows the main entities and their relationships, including Fantasy, Athletes, and additional sub-sections. Use this to guide ORM class design and API traversal.

```
Sport
 └─ League
     └─ Season
         ├─ Team
         │   ├─ Athletes
         │   │   └─ EventLog / Stats / Gamelog
         │   ├─ Events
         │   │   └─ Competition
         │   │       ├─ Roster
         │   │       ├─ Plays
         │   │       ├─ Statistics
         │   │       └─ Odds
         │   ├─ Injuries
         │   └─ Depthcharts
         ├─ Draft
         ├─ Calendar
         ├─ Venues
         ├─ News
         ├─ Groups / Standings
         └─ Fantasy
             ├─ Players
             ├─ Teams
             └─ Leagues
```

### Not Yet Implemented (Suggested ORM Classes)

- `FantasyAPI` (for fantasy endpoints)
- `DraftAPI` (for draft endpoints)
- `OddsAPI` (for betting endpoints)
- `InjuryAPI` (for team/athlete injuries)
- `VenueAPI` (for venue endpoints)
- `NewsAPI` (for news endpoints)
- `GroupAPI` (for groups/standings)
- `PlayAPI` (for play-by-play endpoints)

---

## Example Traversal (AI Agent)

1. **Start at Sport (football)**
2. **Get League (NFL)**
3. **Get Season (2025, regular)**
4. **List Teams**
5. **For each Team, get Athletes, Events, Injuries, Depthcharts**
6. **For each Athlete, get EventLog, Statistics, Gamelog**
7. **For each Event, get Competition, Plays, Roster, Odds**
8. **For Fantasy, get Players, Teams, League info using views**
9. **For Draft, get Draft info for season**
10. **For News, get news for league, team, or athlete**


**See also:** [ESPN API Interaction Instructions](.github/instructions/espn-api.instructions.md)

## Copilot Reviewer Guidelines

When reviewing code or suggestions for this repository, Copilot Reviewer should:

1. **Prioritize API Coverage:**
   - Ensure new endpoints/classes are mapped to ESPN API URLs as documented in the gist.
   - Confirm that new features or changes maintain or improve coverage for NFL and other sports.

2. **Maintain ORM-Like Structure:**
   - All new API classes **must inherit from `ESPNBaseAPI`** (see `espn_api_orm/generic/api.py`) and follow the established encapsulation pattern.
   - Bind API endpoints to Python classes and methods, following the inheritance chain (e.g., `ESPNBaseAPI -> ESPNSportAPI -> ESPNLeagueAPI -> ESPNSeasonAPI -> ESPNTeamAPI`).
   - Avoid direct HTTP requests in user code; encapsulate them in API classes.
   - Use the `_core_url` and `_base_url` attributes from the base class for endpoint construction, and always use the `api_request` method for HTTP calls.

3. **Documentation & Examples:**
   - Require docstrings for all public classes and methods.
   - Encourage updates to the README and `examples/` for new features or endpoints.

4. **Testing:**
   - Ensure new code is covered by unit tests in the `tests/` directory.
   - Prefer pytest for all test cases.

5. **Code Quality:**
   - Enforce PEP8 style and clear, maintainable code.
   - Avoid hardcoding endpoint URLs; use constants or configuration.

6. **Extensibility:**
   - Design new features to support other sports/leagues (not just NFL).
   - Use parameters (e.g., `{YEAR}`, `{TEAM_ID}`) as described in the gist for flexibility.

## Example Use Cases

- **Retrieve NFL Team Roster:**
  ```python
  from espn_api_orm.team.api import TeamAPI
  team = TeamAPI(team_id=4, season=2023)
  roster = team.get_roster()
  ```

- **Get Season Calendar:**
  ```python
  from espn_api_orm.calendar.api import CalendarAPI
  calendar = CalendarAPI(season=2023)
  weeks = calendar.get_weeks()
  ```

- **Fetch Scoreboard Data:**
  ```python
  from espn_api_orm.scoreboard.api import ScoreboardAPI
  scoreboard = ScoreboardAPI(season=2023, week=1)
  games = scoreboard.get_games()
  ```

- **List All Athletes for a Team:**
  ```python
  from espn_api_orm.team.api import TeamAPI
  team = TeamAPI(team_id=18, season=2023)
  athletes = team.get_athletes()
  ```

- **Get Event Details:**
  ```python
  from espn_api_orm.event.api import EventAPI
  event = EventAPI(event_id=401326315)
  details = event.get_details()
  ```

---

For more endpoint details, see the [API gist](https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c) and the README.
