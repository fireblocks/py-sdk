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

from fireblocks.models.asset_response_onchain import AssetResponseOnchain


class TestAssetResponseOnchain(unittest.TestCase):
    """AssetResponseOnchain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetResponseOnchain:
        """Test AssetResponseOnchain
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AssetResponseOnchain`
        """
        model = AssetResponseOnchain()
        if include_optional:
            return AssetResponseOnchain(
                symbol = 'TST3',
                name = 'Test 3',
                address = '0xe7A9as1oa38bc4da0248s179E30aa94CcF453991',
                decimals = 18,
                standard = 'ERC20'
            )
        else:
            return AssetResponseOnchain(
                symbol = 'TST3',
                name = 'Test 3',
                decimals = 18,
        )
        """

    def testAssetResponseOnchain(self):
        """Test AssetResponseOnchain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
