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

from fireblocks.models.set_customer_ref_id_for_address_request import (
    SetCustomerRefIdForAddressRequest,
)


class TestSetCustomerRefIdForAddressRequest(unittest.TestCase):
    """SetCustomerRefIdForAddressRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetCustomerRefIdForAddressRequest:
        """Test SetCustomerRefIdForAddressRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SetCustomerRefIdForAddressRequest`
        """
        model = SetCustomerRefIdForAddressRequest()
        if include_optional:
            return SetCustomerRefIdForAddressRequest(
                customer_ref_id = ''
            )
        else:
            return SetCustomerRefIdForAddressRequest(
        )
        """

    def testSetCustomerRefIdForAddressRequest(self):
        """Test SetCustomerRefIdForAddressRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
