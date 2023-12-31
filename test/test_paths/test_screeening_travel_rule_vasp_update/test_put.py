# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 
    Contact: support@fireblocks.com
    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import fireblocks_client
from fireblocks_client.paths.screeening_travel_rule_vasp_update import put  # noqa: E501
from fireblocks_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestScreeeningTravelRuleVaspUpdate(ApiTestMixin, unittest.TestCase):
    """
    ScreeeningTravelRuleVaspUpdate unit test stubs
        Add jsonDidKey to VASP details  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
