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

from fireblocks.models.add_asset_to_external_wallet_request_one_of1_additional_info_one_of import (
    AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf,
)


class TestAddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf(unittest.TestCase):
    """AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf:
        """Test AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf`
        """
        model = AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf()
        if include_optional:
            return AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf(
                account_holder_given_name = '',
                account_holder_surname = '',
                account_holder_city = '',
                account_holder_country = '',
                account_holder_address1 = '',
                account_holder_address2 = '',
                account_holder_district = '',
                account_holder_postal_code = '',
                iban = '',
                iban_city = '',
                iban_country = ''
            )
        else:
            return AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf(
                account_holder_given_name = '',
                account_holder_city = '',
                account_holder_country = '',
                account_holder_address1 = '',
                account_holder_postal_code = '',
                iban = '',
                iban_city = '',
                iban_country = '',
        )
        """

    def testAddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf(self):
        """Test AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
