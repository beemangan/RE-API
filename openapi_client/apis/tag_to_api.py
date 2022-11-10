import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.event_api import EventApi
from openapi_client.apis.tags.program_api import ProgramApi
from openapi_client.apis.tags.season_api import SeasonApi
from openapi_client.apis.tags.team_api import TeamApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EVENT: EventApi,
        TagValues.PROGRAM: ProgramApi,
        TagValues.SEASON: SeasonApi,
        TagValues.TEAM: TeamApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EVENT: EventApi,
        TagValues.PROGRAM: ProgramApi,
        TagValues.SEASON: SeasonApi,
        TagValues.TEAM: TeamApi,
    }
)
