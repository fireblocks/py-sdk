# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import fireblocks_client
from fireblocks_client.paths.vault_accounts_vault_account_id_set_customer_ref_id import post  # noqa: E501
from fireblocks_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestVaultAccountsVaultAccountIdSetCustomerRefId(ApiTestMixin, unittest.TestCase):
    """
    VaultAccountsVaultAccountIdSetCustomerRefId unit test stubs
        Set an AML/KYT customer reference ID for a vault account  # noqa: E501
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
