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

from fireblocks.models.create_transaction_response import CreateTransactionResponse


class TestCreateTransactionResponse(unittest.TestCase):
    """CreateTransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTransactionResponse:
        """Test CreateTransactionResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateTransactionResponse`
        """
        model = CreateTransactionResponse()
        if include_optional:
            return CreateTransactionResponse(
                id = '',
                status = '',
                system_messages = fireblocks.models.system_message_info.SystemMessageInfo(
                    type = 'WARN', 
                    message = 'Slow transaction processing. Outgoing transactions might be stuck.', )
            )
        else:
            return CreateTransactionResponse(
        )
        """

    def testCreateTransactionResponse(self):
        """Test CreateTransactionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()