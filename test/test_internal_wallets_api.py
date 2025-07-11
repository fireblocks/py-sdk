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

from fireblocks.api.internal_wallets_api import InternalWalletsApi


class TestInternalWalletsApi(unittest.TestCase):
    """InternalWalletsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InternalWalletsApi()

    def tearDown(self) -> None:
        pass

    def test_create_internal_wallet(self) -> None:
        """Test case for create_internal_wallet

        Create an internal wallet
        """
        pass

    def test_create_internal_wallet_asset(self) -> None:
        """Test case for create_internal_wallet_asset

        Add an asset to an internal wallet
        """
        pass

    def test_delete_internal_wallet(self) -> None:
        """Test case for delete_internal_wallet

        Delete an internal wallet
        """
        pass

    def test_delete_internal_wallet_asset(self) -> None:
        """Test case for delete_internal_wallet_asset

        Delete a whitelisted address
        """
        pass

    def test_get_internal_wallet(self) -> None:
        """Test case for get_internal_wallet

        Get an asset from an internal wallet
        """
        pass

    def test_get_internal_wallet_asset(self) -> None:
        """Test case for get_internal_wallet_asset

        Get an asset from an internal wallet
        """
        pass

    def test_get_internal_wallet_assets_paginated(self) -> None:
        """Test case for get_internal_wallet_assets_paginated

        List assets in an internal wallet (Paginated)
        """
        pass

    def test_get_internal_wallets(self) -> None:
        """Test case for get_internal_wallets

        List internal wallets
        """
        pass

    def test_set_customer_ref_id_for_internal_wallet(self) -> None:
        """Test case for set_customer_ref_id_for_internal_wallet

        Set an AML/KYT customer reference ID for an internal wallet
        """
        pass


if __name__ == "__main__":
    unittest.main()
