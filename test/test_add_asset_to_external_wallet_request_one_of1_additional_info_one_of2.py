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

from fireblocks.models.add_asset_to_external_wallet_request_one_of1_additional_info_one_of2 import (
    AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2,
)


class TestAddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2(unittest.TestCase):
    """AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2:
        """Test AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2`
        """
        model = AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2()
        if include_optional:
            return AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2(
                spei_clabe = '',
                spei_name = ''
            )
        else:
            return AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2(
                spei_clabe = '',
        )
        """

    def testAddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2(self):
        """Test AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()