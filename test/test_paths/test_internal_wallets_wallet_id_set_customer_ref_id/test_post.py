# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import fireblocks_client
from fireblocks_client.paths.internal_wallets_wallet_id_set_customer_ref_id import post  # noqa: E501
from fireblocks_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestInternalWalletsWalletIdSetCustomerRefId(ApiTestMixin, unittest.TestCase):
    """
    InternalWalletsWalletIdSetCustomerRefId unit test stubs
        Set an AML/KYT customer reference ID for an internal wallet  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201
    response_body = ''




if __name__ == '__main__':
    unittest.main()