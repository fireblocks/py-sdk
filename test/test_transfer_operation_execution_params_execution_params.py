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

from fireblocks_client.models.transfer_operation_execution_params_execution_params import (
    TransferOperationExecutionParamsExecutionParams,
)


class TestTransferOperationExecutionParamsExecutionParams(unittest.TestCase):
    """TransferOperationExecutionParamsExecutionParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> TransferOperationExecutionParamsExecutionParams:
        """Test TransferOperationExecutionParamsExecutionParams
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TransferOperationExecutionParamsExecutionParams`
        """
        model = TransferOperationExecutionParamsExecutionParams()
        if include_optional:
            return TransferOperationExecutionParamsExecutionParams(
                amount = '',
                asset_id = '',
                source = fireblocks_client.models.account.Account(
                    account_id = '', 
                    account_type = 'EXCHANGE_ACCOUNT', ),
                destination = None
            )
        else:
            return TransferOperationExecutionParamsExecutionParams(
        )
        """

    def testTransferOperationExecutionParamsExecutionParams(self):
        """Test TransferOperationExecutionParamsExecutionParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
