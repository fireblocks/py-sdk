# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import fireblocks_client
from fireblocks_client.paths.internal_wallets_wallet_id_asset_id import delete  # noqa: E501
from fireblocks_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestInternalWalletsWalletIdAssetId(ApiTestMixin, unittest.TestCase):
    """
    InternalWalletsWalletIdAssetId unit test stubs
        Delete a whitelisted address from an internal wallet  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201
    response_body = ''


if __name__ == '__main__':
    unittest.main()
