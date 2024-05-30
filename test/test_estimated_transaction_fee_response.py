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

from fireblocks_client.models.estimated_transaction_fee_response import (
    EstimatedTransactionFeeResponse,
)


class TestEstimatedTransactionFeeResponse(unittest.TestCase):
    """EstimatedTransactionFeeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimatedTransactionFeeResponse:
        """Test EstimatedTransactionFeeResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EstimatedTransactionFeeResponse`
        """
        model = EstimatedTransactionFeeResponse()
        if include_optional:
            return EstimatedTransactionFeeResponse(
                low = fireblocks_client.models.transaction_fee.TransactionFee(
                    fee_per_byte = '', 
                    gas_price = 1.337, 
                    gas_limit = '', 
                    network_fee = '', 
                    base_fee = 1.337, 
                    priority_fee = 1.337, 
                    max_fee_per_gas_delta = '', 
                    l1_fee = '', ),
                medium = fireblocks_client.models.transaction_fee.TransactionFee(
                    fee_per_byte = '', 
                    gas_price = 1.337, 
                    gas_limit = '', 
                    network_fee = '', 
                    base_fee = 1.337, 
                    priority_fee = 1.337, 
                    max_fee_per_gas_delta = '', 
                    l1_fee = '', ),
                high = fireblocks_client.models.transaction_fee.TransactionFee(
                    fee_per_byte = '', 
                    gas_price = 1.337, 
                    gas_limit = '', 
                    network_fee = '', 
                    base_fee = 1.337, 
                    priority_fee = 1.337, 
                    max_fee_per_gas_delta = '', 
                    l1_fee = '', )
            )
        else:
            return EstimatedTransactionFeeResponse(
                low = fireblocks_client.models.transaction_fee.TransactionFee(
                    fee_per_byte = '', 
                    gas_price = 1.337, 
                    gas_limit = '', 
                    network_fee = '', 
                    base_fee = 1.337, 
                    priority_fee = 1.337, 
                    max_fee_per_gas_delta = '', 
                    l1_fee = '', ),
                medium = fireblocks_client.models.transaction_fee.TransactionFee(
                    fee_per_byte = '', 
                    gas_price = 1.337, 
                    gas_limit = '', 
                    network_fee = '', 
                    base_fee = 1.337, 
                    priority_fee = 1.337, 
                    max_fee_per_gas_delta = '', 
                    l1_fee = '', ),
                high = fireblocks_client.models.transaction_fee.TransactionFee(
                    fee_per_byte = '', 
                    gas_price = 1.337, 
                    gas_limit = '', 
                    network_fee = '', 
                    base_fee = 1.337, 
                    priority_fee = 1.337, 
                    max_fee_per_gas_delta = '', 
                    l1_fee = '', ),
        )
        """

    def testEstimatedTransactionFeeResponse(self):
        """Test EstimatedTransactionFeeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
