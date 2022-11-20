"""
    Wrappers for the API to simplify use.
"""

import rec.configuration as c
import rec.api_client as api
from rec.apis.tags import program_api,season_api,event_api,team_api

class Connector:
    """ Connector object to handle API requests. """
    def __init__(self,key):
        config = c.Configuration()
        config.access_token = str(key)
        client = api.ApiClient(config)

        self.Program = program_api.ProgramApi(client)
        self.Season = season_api.SeasonApi(client)
        self.Event = event_api.EventApi(client)
        self.Team = team_api.TeamApi(client)
