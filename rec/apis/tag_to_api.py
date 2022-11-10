import typing_extensions

from rec.apis.tags import TagValues
from rec.apis.tags.event_api import EventApi
from rec.apis.tags.program_api import ProgramApi
from rec.apis.tags.season_api import SeasonApi
from rec.apis.tags.team_api import TeamApi

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
