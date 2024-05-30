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

from fireblocks.api.external_wallets_api import ExternalWalletsApi


class TestExternalWalletsApi(unittest.TestCase):
    """ExternalWalletsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ExternalWalletsApi()

    def tearDown(self) -> None:
        pass

    def test_add_asset_to_external_wallet(self) -> None:
        """Test case for add_asset_to_external_wallet

        Add an asset to an external wallet.
        """
        pass

    def test_create_external_wallet(self) -> None:
        """Test case for create_external_wallet

        Create an external wallet
        """
        pass

    def test_delete_external_wallet(self) -> None:
        """Test case for delete_external_wallet

        Delete an external wallet
        """
        pass

    def test_get_external_wallet(self) -> None:
        """Test case for get_external_wallet

        Find an external wallet
        """
        pass

    def test_get_external_wallet_asset(self) -> None:
        """Test case for get_external_wallet_asset

        Get an asset from an external wallet
        """
        pass

    def test_get_external_wallets(self) -> None:
        """Test case for get_external_wallets

        List external wallets
        """
        pass

    def test_remove_asset_from_external_wallet(self) -> None:
        """Test case for remove_asset_from_external_wallet

        Delete an asset from an external wallet
        """
        pass

    def test_set_external_wallet_customer_ref_id(self) -> None:
        """Test case for set_external_wallet_customer_ref_id

        Set an AML customer reference ID for an external wallet
        """
        pass


if __name__ == "__main__":
    unittest.main()
