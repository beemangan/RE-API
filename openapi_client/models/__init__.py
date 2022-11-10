# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.alliance import Alliance
from openapi_client.model.alliance_team import AllianceTeam
from openapi_client.model.award import Award
from openapi_client.model.coordinates import Coordinates
from openapi_client.model.division import Division
from openapi_client.model.error import Error
from openapi_client.model.event import Event
from openapi_client.model.event_level import EventLevel
from openapi_client.model.event_type import EventType
from openapi_client.model.grade import Grade
from openapi_client.model.id_info import IdInfo
from openapi_client.model.location import Location
from openapi_client.model.match_obj import MatchObj
from openapi_client.model.page_meta import PageMeta
from openapi_client.model.paginated_award import PaginatedAward
from openapi_client.model.paginated_event import PaginatedEvent
from openapi_client.model.paginated_match import PaginatedMatch
from openapi_client.model.paginated_program import PaginatedProgram
from openapi_client.model.paginated_ranking import PaginatedRanking
from openapi_client.model.paginated_season import PaginatedSeason
from openapi_client.model.paginated_skill import PaginatedSkill
from openapi_client.model.paginated_team import PaginatedTeam
from openapi_client.model.program import Program
from openapi_client.model.ranking import Ranking
from openapi_client.model.season import Season
from openapi_client.model.skill import Skill
from openapi_client.model.skill_type import SkillType
from openapi_client.model.team import Team
from openapi_client.model.team_award_winner import TeamAwardWinner
