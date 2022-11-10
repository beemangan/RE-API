# coding: utf-8

"""
    Public Robot Events API

    An API to access data on Robot Events officially. ## Request Metadata Pagination is performed the same way throughout each pageable endpoint using the query parameters `page` and `per_page`. Please not that dates should be formatted according to RFC3339.   # noqa: E501

    The version of the OpenAPI document: 1.0.21
    Generated by: https://openapi-generator.tech
"""

import unittest

import openapi_client
from openapi_client.model.team_award_winner import TeamAwardWinner
from openapi_client import configuration


class TestTeamAwardWinner(unittest.TestCase):
    """TeamAwardWinner unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()
