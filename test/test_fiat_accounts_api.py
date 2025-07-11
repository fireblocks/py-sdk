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

from fireblocks.api.fiat_accounts_api import FiatAccountsApi


class TestFiatAccountsApi(unittest.TestCase):
    """FiatAccountsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FiatAccountsApi()

    def tearDown(self) -> None:
        pass

    def test_deposit_funds_from_linked_dda(self) -> None:
        """Test case for deposit_funds_from_linked_dda

        Deposit funds from DDA
        """
        pass

    def test_get_fiat_account(self) -> None:
        """Test case for get_fiat_account

        Find a specific fiat account
        """
        pass

    def test_get_fiat_accounts(self) -> None:
        """Test case for get_fiat_accounts

        List fiat accounts
        """
        pass

    def test_redeem_funds_to_linked_dda(self) -> None:
        """Test case for redeem_funds_to_linked_dda

        Redeem funds to DDA
        """
        pass


if __name__ == "__main__":
    unittest.main()
