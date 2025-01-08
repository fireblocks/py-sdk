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

from fireblocks.models.asset_metadata_beta import AssetMetadataBeta


class TestAssetMetadataBeta(unittest.TestCase):
    """AssetMetadataBeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetMetadataBeta:
        """Test AssetMetadataBeta
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AssetMetadataBeta`
        """
        model = AssetMetadataBeta()
        if include_optional:
            return AssetMetadataBeta(
                scope = 'Global',
                deprecated = False,
                deprecation_referral_id = '056776ab-9efa-4219-9820-9ece0cc4d90d',
                verified = True,
                website = 'https://example.org',
                media = [
                    fireblocks.models.asset_media.AssetMedia(
                        url = 'https://example.com/image.png', 
                        type = 'image/svg+xml', 
                        attributes = fireblocks.models.asset_media_attributes.AssetMedia_attributes(
                            monochrome = True, ), )
                    ]
            )
        else:
            return AssetMetadataBeta(
                scope = 'Global',
                deprecated = False,
                verified = True,
        )
        """

    def testAssetMetadataBeta(self):
        """Test AssetMetadataBeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
