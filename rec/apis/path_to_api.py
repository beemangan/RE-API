import typing_extensions

from rec.paths import PathValues
from rec.apis.paths.events import Events
from rec.apis.paths.events_id import EventsId
from rec.apis.paths.events_id_teams import EventsIdTeams
from rec.apis.paths.events_id_skills import EventsIdSkills
from rec.apis.paths.events_id_awards import EventsIdAwards
from rec.apis.paths.events_id_divisions_div_matches import EventsIdDivisionsDivMatches
from rec.apis.paths.events_id_divisions_div_finalist_rankings import EventsIdDivisionsDivFinalistRankings
from rec.apis.paths.events_id_divisions_div_rankings import EventsIdDivisionsDivRankings
from rec.apis.paths.teams import Teams
from rec.apis.paths.teams_id import TeamsId
from rec.apis.paths.teams_id_events import TeamsIdEvents
from rec.apis.paths.teams_id_matches import TeamsIdMatches
from rec.apis.paths.teams_id_rankings import TeamsIdRankings
from rec.apis.paths.teams_id_skills import TeamsIdSkills
from rec.apis.paths.teams_id_awards import TeamsIdAwards
from rec.apis.paths.programs_id import ProgramsId
from rec.apis.paths.programs import Programs
from rec.apis.paths.seasons import Seasons
from rec.apis.paths.seasons_id import SeasonsId
from rec.apis.paths.seasons_id_events import SeasonsIdEvents

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.EVENTS: Events,
        PathValues.EVENTS_ID: EventsId,
        PathValues.EVENTS_ID_TEAMS: EventsIdTeams,
        PathValues.EVENTS_ID_SKILLS: EventsIdSkills,
        PathValues.EVENTS_ID_AWARDS: EventsIdAwards,
        PathValues.EVENTS_ID_DIVISIONS_DIV_MATCHES: EventsIdDivisionsDivMatches,
        PathValues.EVENTS_ID_DIVISIONS_DIV_FINALIST_RANKINGS: EventsIdDivisionsDivFinalistRankings,
        PathValues.EVENTS_ID_DIVISIONS_DIV_RANKINGS: EventsIdDivisionsDivRankings,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.TEAMS_ID_EVENTS: TeamsIdEvents,
        PathValues.TEAMS_ID_MATCHES: TeamsIdMatches,
        PathValues.TEAMS_ID_RANKINGS: TeamsIdRankings,
        PathValues.TEAMS_ID_SKILLS: TeamsIdSkills,
        PathValues.TEAMS_ID_AWARDS: TeamsIdAwards,
        PathValues.PROGRAMS_ID: ProgramsId,
        PathValues.PROGRAMS: Programs,
        PathValues.SEASONS: Seasons,
        PathValues.SEASONS_ID: SeasonsId,
        PathValues.SEASONS_ID_EVENTS: SeasonsIdEvents,
    }
)

path_to_api = PathToApi(
    {
        PathValues.EVENTS: Events,
        PathValues.EVENTS_ID: EventsId,
        PathValues.EVENTS_ID_TEAMS: EventsIdTeams,
        PathValues.EVENTS_ID_SKILLS: EventsIdSkills,
        PathValues.EVENTS_ID_AWARDS: EventsIdAwards,
        PathValues.EVENTS_ID_DIVISIONS_DIV_MATCHES: EventsIdDivisionsDivMatches,
        PathValues.EVENTS_ID_DIVISIONS_DIV_FINALIST_RANKINGS: EventsIdDivisionsDivFinalistRankings,
        PathValues.EVENTS_ID_DIVISIONS_DIV_RANKINGS: EventsIdDivisionsDivRankings,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.TEAMS_ID_EVENTS: TeamsIdEvents,
        PathValues.TEAMS_ID_MATCHES: TeamsIdMatches,
        PathValues.TEAMS_ID_RANKINGS: TeamsIdRankings,
        PathValues.TEAMS_ID_SKILLS: TeamsIdSkills,
        PathValues.TEAMS_ID_AWARDS: TeamsIdAwards,
        PathValues.PROGRAMS_ID: ProgramsId,
        PathValues.PROGRAMS: Programs,
        PathValues.SEASONS: Seasons,
        PathValues.SEASONS_ID: SeasonsId,
        PathValues.SEASONS_ID_EVENTS: SeasonsIdEvents,
    }
)
