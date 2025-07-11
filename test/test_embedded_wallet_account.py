# coding: utf-8

"""
Fireblocks API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.6.2
Contact: support@fireblocks.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from fireblocks.models.embedded_wallet_account import EmbeddedWalletAccount


class TestEmbeddedWalletAccount(unittest.TestCase):
    """EmbeddedWalletAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmbeddedWalletAccount:
        """Test EmbeddedWalletAccount
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EmbeddedWalletAccount`
        """
        model = EmbeddedWalletAccount()
        if include_optional:
            return EmbeddedWalletAccount(
                account_id = '0',
                wallet_id = '550e8400-e29b-41d4-a716-446655440000'
            )
        else:
            return EmbeddedWalletAccount(
                account_id = '0',
                wallet_id = '550e8400-e29b-41d4-a716-446655440000',
        )
        """

    def testEmbeddedWalletAccount(self):
        """Test EmbeddedWalletAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
