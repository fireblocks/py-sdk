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

from fireblocks.models.asset import Asset


class TestAsset(unittest.TestCase):
    """Asset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Asset:
        """Test Asset
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Asset`
        """
        model = Asset()
        if include_optional:
            return Asset(
                id = '9f9f7062-df90-4fc0-8697-96685184358d',
                legacy_id = 'USDT_ERC20',
                blockchain_id = 'e85208ff-3b15-44e9-af14-0ed0280b2a15',
                display_name = 'Tether USD',
                display_symbol = 'USDT',
                asset_class = 'FT',
                onchain = fireblocks.models.asset_details_onchain.AssetDetailsOnchain(
                    symbol = 'USDT', 
                    name = 'Tether USD', 
                    address = '0xdAC17F958D2ee523a2206206994597C13D831ec7', 
                    decimals = 6, 
                    standards = ["ERC20"], ),
                metadata = fireblocks.models.asset_details_metadata.AssetDetailsMetadata(
                    scope = 'GLOBAL', 
                    verified = False, 
                    deprecated = False, 
                    deprecation_referral_id = '056776ab-9efa-4219-9820-9ece0cc4d90d', 
                    website = 'https://example.org', 
                    media = [
                        fireblocks.models.asset_media.AssetMedia(
                            url = 'https://example.com/image.png', 
                            type = 'image/svg+xml', 
                            attributes = fireblocks.models.asset_media_attributes.AssetMedia_attributes(
                                monochrome = True, ), )
                        ], 
                    note = fireblocks.models.asset_note.AssetNote(
                        text = 'Pay attention to gas fees', 
                        user_id = '056776ab-9efa-4219-9820-9ece0cc4d90d', 
                        user_name = 'Test test', 
                        updated_at = '2025-06-08T19:42:49Z', ), )
            )
        else:
            return Asset(
                id = '9f9f7062-df90-4fc0-8697-96685184358d',
                legacy_id = 'USDT_ERC20',
                display_name = 'Tether USD',
                display_symbol = 'USDT',
                asset_class = 'FT',
                metadata = fireblocks.models.asset_details_metadata.AssetDetailsMetadata(
                    scope = 'GLOBAL', 
                    verified = False, 
                    deprecated = False, 
                    deprecation_referral_id = '056776ab-9efa-4219-9820-9ece0cc4d90d', 
                    website = 'https://example.org', 
                    media = [
                        fireblocks.models.asset_media.AssetMedia(
                            url = 'https://example.com/image.png', 
                            type = 'image/svg+xml', 
                            attributes = fireblocks.models.asset_media_attributes.AssetMedia_attributes(
                                monochrome = True, ), )
                        ], 
                    note = fireblocks.models.asset_note.AssetNote(
                        text = 'Pay attention to gas fees', 
                        user_id = '056776ab-9efa-4219-9820-9ece0cc4d90d', 
                        user_name = 'Test test', 
                        updated_at = '2025-06-08T19:42:49Z', ), ),
        )
        """

    def testAsset(self):
        """Test Asset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
