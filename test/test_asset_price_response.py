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

from fireblocks.models.asset_price_response import AssetPriceResponse


class TestAssetPriceResponse(unittest.TestCase):
    """AssetPriceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetPriceResponse:
        """Test AssetPriceResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AssetPriceResponse`
        """
        model = AssetPriceResponse()
        if include_optional:
            return AssetPriceResponse(
                legacy_id = 'ETH',
                last_update_at = 1716898542,
                currency = 'USD',
                price = 3500,
                source = 'PRIVATE'
            )
        else:
            return AssetPriceResponse(
                legacy_id = 'ETH',
                last_update_at = 1716898542,
                currency = 'USD',
                price = 3500,
                source = 'PRIVATE',
        )
        """

    def testAssetPriceResponse(self):
        """Test AssetPriceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
