import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.events import Events
from openapi_client.apis.paths.events_id import EventsId
from openapi_client.apis.paths.events_id_teams import EventsIdTeams
from openapi_client.apis.paths.events_id_skills import EventsIdSkills
from openapi_client.apis.paths.events_id_awards import EventsIdAwards
from openapi_client.apis.paths.events_id_divisions_div_matches import EventsIdDivisionsDivMatches
from openapi_client.apis.paths.events_id_divisions_div_finalist_rankings import EventsIdDivisionsDivFinalistRankings
from openapi_client.apis.paths.events_id_divisions_div_rankings import EventsIdDivisionsDivRankings
from openapi_client.apis.paths.teams import Teams
from openapi_client.apis.paths.teams_id import TeamsId
from openapi_client.apis.paths.teams_id_events import TeamsIdEvents
from openapi_client.apis.paths.teams_id_matches import TeamsIdMatches
from openapi_client.apis.paths.teams_id_rankings import TeamsIdRankings
from openapi_client.apis.paths.teams_id_skills import TeamsIdSkills
from openapi_client.apis.paths.teams_id_awards import TeamsIdAwards
from openapi_client.apis.paths.programs_id import ProgramsId
from openapi_client.apis.paths.programs import Programs
from openapi_client.apis.paths.seasons import Seasons
from openapi_client.apis.paths.seasons_id import SeasonsId
from openapi_client.apis.paths.seasons_id_events import SeasonsIdEvents

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
