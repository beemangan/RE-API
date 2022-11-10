# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rec.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    EVENTS = "/events"
    EVENTS_ID = "/events/{id}"
    EVENTS_ID_TEAMS = "/events/{id}/teams"
    EVENTS_ID_SKILLS = "/events/{id}/skills"
    EVENTS_ID_AWARDS = "/events/{id}/awards"
    EVENTS_ID_DIVISIONS_DIV_MATCHES = "/events/{id}/divisions/{div}/matches"
    EVENTS_ID_DIVISIONS_DIV_FINALIST_RANKINGS = "/events/{id}/divisions/{div}/finalistRankings"
    EVENTS_ID_DIVISIONS_DIV_RANKINGS = "/events/{id}/divisions/{div}/rankings"
    TEAMS = "/teams"
    TEAMS_ID = "/teams/{id}"
    TEAMS_ID_EVENTS = "/teams/{id}/events"
    TEAMS_ID_MATCHES = "/teams/{id}/matches"
    TEAMS_ID_RANKINGS = "/teams/{id}/rankings"
    TEAMS_ID_SKILLS = "/teams/{id}/skills"
    TEAMS_ID_AWARDS = "/teams/{id}/awards"
    PROGRAMS_ID = "/programs/{id}"
    PROGRAMS = "/programs"
    SEASONS = "/seasons"
    SEASONS_ID = "/seasons/{id}"
    SEASONS_ID_EVENTS = "/seasons/{id}/events"
