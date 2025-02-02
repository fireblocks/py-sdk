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

from fireblocks.models.add_exchange_account_request import AddExchangeAccountRequest


class TestAddExchangeAccountRequest(unittest.TestCase):
    """AddExchangeAccountRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddExchangeAccountRequest:
        """Test AddExchangeAccountRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AddExchangeAccountRequest`
        """
        model = AddExchangeAccountRequest()
        if include_optional:
            return AddExchangeAccountRequest(
                exchange_type = 'INDEPENDENT_RESERVE',
                name = '',
                creds = '',
                key = '',
                main_account_id = ''
            )
        else:
            return AddExchangeAccountRequest(
                exchange_type = 'INDEPENDENT_RESERVE',
                name = '',
        )
        """

    def testAddExchangeAccountRequest(self):
        """Test AddExchangeAccountRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
