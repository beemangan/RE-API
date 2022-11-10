# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from rec.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from rec.model.alliance import Alliance
from rec.model.alliance_team import AllianceTeam
from rec.model.award import Award
from rec.model.coordinates import Coordinates
from rec.model.division import Division
from rec.model.error import Error
from rec.model.event import Event
from rec.model.event_level import EventLevel
from rec.model.event_type import EventType
from rec.model.grade import Grade
from rec.model.id_info import IdInfo
from rec.model.location import Location
from rec.model.match_obj import MatchObj
from rec.model.page_meta import PageMeta
from rec.model.paginated_award import PaginatedAward
from rec.model.paginated_event import PaginatedEvent
from rec.model.paginated_match import PaginatedMatch
from rec.model.paginated_program import PaginatedProgram
from rec.model.paginated_ranking import PaginatedRanking
from rec.model.paginated_season import PaginatedSeason
from rec.model.paginated_skill import PaginatedSkill
from rec.model.paginated_team import PaginatedTeam
from rec.model.program import Program
from rec.model.ranking import Ranking
from rec.model.season import Season
from rec.model.skill import Skill
from rec.model.skill_type import SkillType
from rec.model.team import Team
from rec.model.team_award_winner import TeamAwardWinner
