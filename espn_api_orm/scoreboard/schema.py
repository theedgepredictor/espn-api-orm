##################################
# Scoreboard Classes
##################################

from typing import List, Optional, Any

from pydantic import BaseModel
import datetime

from espn_api_orm.generic.schema import Day, Logo, Link


class League(BaseModel):
    id: str
    uid: str
    name: str
    abbreviation: str
    midsizeName: Optional[str] = None
    slug: str
    season: 'Season'
    logos: List[Logo]
    calendarType: str
    calendarIsWhitelist: bool
    calendarStartDate: datetime.datetime
    calendarEndDate: datetime.datetime
    calendar: List[Any]

    class Season(BaseModel):
        year: int
        startDate: datetime.datetime
        endDate: datetime.datetime
        displayName: str
        type: 'SeasonType'

        class SeasonType(BaseModel):
            id: int
            type: int
            name: str
            abbreviation: str


## Day
class TeamRef(BaseModel):
    id: int


class VenueRef(BaseModel):
    id: int


class EventDate(BaseModel):
    date: datetime.datetime
    seasonType: int


## Events


class Athlete(BaseModel):
    id: str
    fullName: str
    displayName: str
    shortName: str
    links: List[Link]
    headshot: Optional[str] = None
    jersey: Optional[str] = None
    position: 'Position'
    team: 'TeamRef'
    active: bool

    class Position(BaseModel):
        abbreviation: str


class Address(BaseModel):
    city: str
    state: Optional[str] = None


class CuratedRank(BaseModel):
    current: int


class Team(BaseModel):
    id: int
    uid: str
    location: str
    name: Optional[str] = None
    abbreviation: str
    displayName: str
    shortDisplayName: str
    color: Optional[str] = None
    alternateColor: Optional[str] = None
    isActive: bool
    venue: Optional['VenueRef'] = None
    links: List['Link']
    logo: Optional[str] = None
    conferenceId: Optional[int] = None


class Competitor(BaseModel):
    id: str
    uid: str
    type: str
    order: int
    homeAway: str
    winner: Optional[bool] = None
    team: 'Team'
    score: str
    linescores: List['Linescore'] = []
    statistics: List['Statistic'] = []
    leaders: List['LeaderGroup'] = []
    curatedRank: Optional[CuratedRank] = None
    records: List['Record'] = []

    class Linescore(BaseModel):
        value: float

    class Statistic(BaseModel):
        name: str
        abbreviation: str
        displayValue: str

    class Record(BaseModel):
        name: str
        abbreviation: Optional[str] = None
        type: str
        summary: str

    class LeaderGroup(BaseModel):
        name: str
        displayName: str
        shortDisplayName: str
        abbreviation: str
        leaders: List['Leader'] = None

        class Leader(BaseModel):
            displayValue: str
            value: float
            athlete: 'Athlete'
            team: 'TeamRef'


class Competition(BaseModel):
    id: str
    uid: str
    date: datetime.datetime
    attendance: Optional[int] = None
    type: Optional['Type'] = None
    timeValid: bool
    neutralSite: bool
    conferenceCompetition: Optional[bool] = None
    playByPlayAvailable: bool
    recent: bool
    venue: Optional['Venue'] = None
    competitors: List[Competitor]

    class Venue(BaseModel):
        id: str
        fullName: str
        address: 'Address'
        capacity: Optional[int] = None
        indoor: Optional[bool] = None

    class Type(BaseModel):
        id: str
        abbreviation: str


class Event(BaseModel):
    id: str
    uid: str
    date: datetime.datetime
    name: str
    shortName: str
    season: 'Season'
    competitions: List[Competition]
    links: List['Link']
    status: 'Status'

    class Status(BaseModel):
        clock: Optional[float] = None
        displayClock: Optional[str] = None
        period: int
        type: 'Type'

        class Type(BaseModel):
            id: str
            name: str
            state: str
            completed: bool
            description: str
            detail: str
            shortDetail: str

    class Season(BaseModel):
        year: int
        type: int
        slug: str


class Scoreboard(BaseModel):
    leagues: List[League]
    groups: List[str] = None
    day: Optional[Day] = None
    eventsDate: Optional[EventDate] = None
    events: List[Event]
