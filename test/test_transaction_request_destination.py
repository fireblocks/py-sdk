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

from fireblocks.models.transaction_request_destination import (
    TransactionRequestDestination,
)


class TestTransactionRequestDestination(unittest.TestCase):
    """TransactionRequestDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionRequestDestination:
        """Test TransactionRequestDestination
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TransactionRequestDestination`
        """
        model = TransactionRequestDestination()
        if include_optional:
            return TransactionRequestDestination(
                amount = '',
                destination = fireblocks.models.destination_transfer_peer_path.DestinationTransferPeerPath(
                    type = 'VAULT_ACCOUNT', 
                    sub_type = 'BINANCE', 
                    id = '', 
                    name = '', 
                    wallet_id = '', 
                    one_time_address = fireblocks.models.one_time_address.OneTimeAddress(
                        address = '', 
                        tag = '', ), )
            )
        else:
            return TransactionRequestDestination(
        )
        """

    def testTransactionRequestDestination(self):
        """Test TransactionRequestDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
