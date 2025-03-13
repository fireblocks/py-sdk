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

from fireblocks.models.transaction_receipt_response import TransactionReceiptResponse


class TestTransactionReceiptResponse(unittest.TestCase):
    """TransactionReceiptResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionReceiptResponse:
        """Test TransactionReceiptResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TransactionReceiptResponse`
        """
        model = TransactionReceiptResponse()
        if include_optional:
            return TransactionReceiptResponse(
                block_hash = '0x6e3c92a3d96f96e46b7f39c30244edb6e8e0f4b65d3846c9f8287f9dd5d1a3d2',
                block_number = 123456,
                contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66',
                cumulative_gas_used = 21000,
                effective_gas_price = 1000000000,
                var_from = '0xa7D9ddBE1f17865597Fbd27ec712455208B6b76D',
                gas_used = 21000,
                logs = [
                    fireblocks.models.tx_log.TxLog(
                        address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66', 
                        topics = ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef","0x000000000000000000000000a7d9ddbe1f17865597fbd27ec712455208b6b76d","0x000000000000000000000000c2c4e1db41f0bb97996d0ed0542d2170d146fb66"], 
                        data = '0x000000000000000000000000000000000000000000000000000000000000000a', 
                        block_number = 123456, 
                        transaction_hash = '0x5a3b7f4b2c9e4a0b1f8a12c8e5f1d0e2a6b4c9d1f7e2b1a2b3c4d5e6f7a8b9c', 
                        transaction_index = 2, 
                        block_hash = '0x6e3c92a3d96f96e46b7f39c30244edb6e8e0f4b65d3846c9f8287f9dd5d1a3d2', 
                        log_index = 1, 
                        removed = False, )
                    ],
                logs_bloom = '0x0000000000000000000000000000000000000000000000000000000000000000',
                status = 1,
                to = '0x1eC4a8bB9bB9Afa24f79cC2e1423cD00B6cFf50',
                transaction_hash = '0x5a3b7f4b2c9e4a0b1f8a12c8e5f1d0e2a6b4c9d1f7e2b1a2b3c4d5e6f7a8b9c',
                transaction_index = 3,
                type = '0x2'
            )
        else:
            return TransactionReceiptResponse(
                block_hash = '0x6e3c92a3d96f96e46b7f39c30244edb6e8e0f4b65d3846c9f8287f9dd5d1a3d2',
                block_number = 123456,
                cumulative_gas_used = 21000,
                effective_gas_price = 1000000000,
                var_from = '0xa7D9ddBE1f17865597Fbd27ec712455208B6b76D',
                gas_used = 21000,
                logs = [
                    fireblocks.models.tx_log.TxLog(
                        address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66', 
                        topics = ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef","0x000000000000000000000000a7d9ddbe1f17865597fbd27ec712455208b6b76d","0x000000000000000000000000c2c4e1db41f0bb97996d0ed0542d2170d146fb66"], 
                        data = '0x000000000000000000000000000000000000000000000000000000000000000a', 
                        block_number = 123456, 
                        transaction_hash = '0x5a3b7f4b2c9e4a0b1f8a12c8e5f1d0e2a6b4c9d1f7e2b1a2b3c4d5e6f7a8b9c', 
                        transaction_index = 2, 
                        block_hash = '0x6e3c92a3d96f96e46b7f39c30244edb6e8e0f4b65d3846c9f8287f9dd5d1a3d2', 
                        log_index = 1, 
                        removed = False, )
                    ],
                logs_bloom = '0x0000000000000000000000000000000000000000000000000000000000000000',
                status = 1,
                transaction_hash = '0x5a3b7f4b2c9e4a0b1f8a12c8e5f1d0e2a6b4c9d1f7e2b1a2b3c4d5e6f7a8b9c',
                transaction_index = 3,
                type = '0x2',
        )
        """

    def testTransactionReceiptResponse(self):
        """Test TransactionReceiptResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
