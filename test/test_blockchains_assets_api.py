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

from fireblocks.api.blockchains_assets_api import BlockchainsAssetsApi


class TestBlockchainsAssetsApi(unittest.TestCase):
    """BlockchainsAssetsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BlockchainsAssetsApi()

    def tearDown(self) -> None:
        pass

    def test_get_supported_assets(self) -> None:
        """Test case for get_supported_assets

        List all asset types supported by Fireblocks
        """
        pass

    def test_register_new_asset(self) -> None:
        """Test case for register_new_asset

        Register an asset
        """
        pass

    def test_set_asset_price(self) -> None:
        """Test case for set_asset_price

        Set asset price
        """
        pass


if __name__ == "__main__":
    unittest.main()
