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

from fireblocks.models.paginated_address_response import PaginatedAddressResponse


class TestPaginatedAddressResponse(unittest.TestCase):
    """PaginatedAddressResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedAddressResponse:
        """Test PaginatedAddressResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PaginatedAddressResponse`
        """
        model = PaginatedAddressResponse()
        if include_optional:
            return PaginatedAddressResponse(
                addresses = [
                    fireblocks.models.vault_wallet_address.VaultWalletAddress(
                        asset_id = '', 
                        address = '', 
                        description = '', 
                        tag = '', 
                        type = '', 
                        customer_ref_id = '', 
                        address_format = 'SEGWIT', 
                        legacy_address = '', 
                        enterprise_address = '', 
                        bip44_address_index = 56, 
                        user_defined = True, )
                    ],
                paging = fireblocks.models.paginated_address_response_paging.PaginatedAddressResponse_paging(
                    before = '', 
                    after = '', )
            )
        else:
            return PaginatedAddressResponse(
        )
        """

    def testPaginatedAddressResponse(self):
        """Test PaginatedAddressResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
