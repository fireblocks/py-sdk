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

from fireblocks.models.wallet_asset_additional_info import WalletAssetAdditionalInfo


class TestWalletAssetAdditionalInfo(unittest.TestCase):
    """WalletAssetAdditionalInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletAssetAdditionalInfo:
        """Test WalletAssetAdditionalInfo
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `WalletAssetAdditionalInfo`
        """
        model = WalletAssetAdditionalInfo()
        if include_optional:
            return WalletAssetAdditionalInfo(
                account_holder_given_name = '',
                account_holder_surname = '',
                account_holder_city = '',
                account_holder_country = '',
                account_holder_address1 = '',
                account_holder_address2 = '',
                account_holder_district = '',
                account_holder_postal_code = '',
                aba_routing_number = '',
                aba_account_number = '',
                aba_country = '',
                iban = '',
                iban_city = '',
                iban_country = '',
                spei_clabe = '',
                spei_name = ''
            )
        else:
            return WalletAssetAdditionalInfo(
        )
        """

    def testWalletAssetAdditionalInfo(self):
        """Test WalletAssetAdditionalInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()