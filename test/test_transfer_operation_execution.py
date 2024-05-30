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

from fireblocks_client.models.transfer_operation_execution import (
    TransferOperationExecution,
)


class TestTransferOperationExecution(unittest.TestCase):
    """TransferOperationExecution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferOperationExecution:
        """Test TransferOperationExecution
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TransferOperationExecution`
        """
        model = TransferOperationExecution()
        if include_optional:
            return TransferOperationExecution(
                input = fireblocks_client.models.transfer_operation_config_params.TransferOperationConfigParams(
                    amount = '', 
                    asset_id = '', 
                    source = fireblocks_client.models.account.Account(
                        account_id = '', 
                        account_type = 'EXCHANGE_ACCOUNT', ), 
                    destination = null, ),
                output = fireblocks_client.models.transfer_operation_execution_output.TransferOperationExecutionOutput(
                    amount = fireblocks_client.models.asset_amount.AssetAmount(
                        amount = '', 
                        asset_id = '', ), 
                    fee = fireblocks_client.models.asset_amount.AssetAmount(
                        amount = '', 
                        asset_id = '', ), ),
                tx_id = '',
                started_at = 1.337,
                finished_at = 1.337,
                failure = fireblocks_client.models.transfer_operation_failure.TransferOperationFailure(
                    reason = 'INVALID_AMOUNT', 
                    data = fireblocks_client.models.transfer_operation_failure_data.TransferOperationFailure_data(
                        tx_id = '', 
                        tx_status = '', 
                        tx_sub_status = '', ), )
            )
        else:
            return TransferOperationExecution(
                input = fireblocks_client.models.transfer_operation_config_params.TransferOperationConfigParams(
                    amount = '', 
                    asset_id = '', 
                    source = fireblocks_client.models.account.Account(
                        account_id = '', 
                        account_type = 'EXCHANGE_ACCOUNT', ), 
                    destination = null, ),
                started_at = 1.337,
        )
        """

    def testTransferOperationExecution(self):
        """Test TransferOperationExecution"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
