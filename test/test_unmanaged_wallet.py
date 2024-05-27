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

from fireblocks_client.models.unmanaged_wallet import UnmanagedWallet


class TestUnmanagedWallet(unittest.TestCase):
    """UnmanagedWallet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnmanagedWallet:
        """Test UnmanagedWallet
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UnmanagedWallet`
        """
        model = UnmanagedWallet()
        if include_optional:
            return UnmanagedWallet(
                id = '',
                name = '',
                customer_ref_id = '',
                assets = [
                    fireblocks_client.models.wallet_asset.WalletAsset(
                        id = '', 
                        balance = '', 
                        locked_amount = '', 
                        status = 'WAITING_FOR_APPROVAL', 
                        address = '', 
                        tag = '', 
                        activation_time = '', )
                    ]
            )
        else:
            return UnmanagedWallet(
                id = '',
                name = '',
                assets = [
                    fireblocks_client.models.wallet_asset.WalletAsset(
                        id = '', 
                        balance = '', 
                        locked_amount = '', 
                        status = 'WAITING_FOR_APPROVAL', 
                        address = '', 
                        tag = '', 
                        activation_time = '', )
                    ],
        )
        """

    def testUnmanagedWallet(self):
        """Test UnmanagedWallet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
