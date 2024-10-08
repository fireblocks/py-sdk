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

from fireblocks.models.transaction_request import TransactionRequest


class TestTransactionRequest(unittest.TestCase):
    """TransactionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionRequest:
        """Test TransactionRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TransactionRequest`
        """
        model = TransactionRequest()
        if include_optional:
            return TransactionRequest(
                operation = 'TRANSFER',
                note = 'Ticket 123',
                external_tx_id = '00000000-0000-0000-0000-000000000000',
                asset_id = 'ETH',
                source = fireblocks.models.source_transfer_peer_path.SourceTransferPeerPath(
                    type = 'VAULT_ACCOUNT', 
                    sub_type = 'BINANCE', 
                    id = '', 
                    name = '', 
                    wallet_id = '', ),
                destination = fireblocks.models.destination_transfer_peer_path.DestinationTransferPeerPath(
                    type = 'VAULT_ACCOUNT', 
                    sub_type = 'BINANCE', 
                    id = '', 
                    name = '', 
                    wallet_id = '', 
                    one_time_address = fireblocks.models.one_time_address.OneTimeAddress(
                        address = '', 
                        tag = '', ), ),
                destinations = [
                    fireblocks.models.transaction_request_destination.TransactionRequestDestination(
                        amount = '', 
                        destination = fireblocks.models.destination_transfer_peer_path.DestinationTransferPeerPath(
                            type = 'VAULT_ACCOUNT', 
                            sub_type = 'BINANCE', 
                            id = '', 
                            name = '', 
                            wallet_id = '', 
                            one_time_address = fireblocks.models.one_time_address.OneTimeAddress(
                                address = '', 
                                tag = '', ), ), )
                    ],
                amount = None,
                treat_as_gross_amount = False,
                force_sweep = False,
                fee_level = 'MEDIUM',
                fee = None,
                priority_fee = None,
                fail_on_low_fee = True,
                max_fee = '120',
                max_total_fee = '88',
                gas_limit = None,
                gas_price = None,
                network_fee = None,
                replace_tx_by_hash = '00000000-0000-0000-0000-000000000000',
                extra_parameters = None,
                customer_ref_id = 'abcdef',
                travel_rule_message = fireblocks.models.travel_rule_create_transaction_request.TravelRuleCreateTransactionRequest(
                    originator_vas_pdid = '', 
                    beneficiary_vas_pdid = '', 
                    beneficiary_vas_pname = '', 
                    transaction_blockchain_info = null, 
                    originator = null, 
                    beneficiary = null, 
                    encrypted = '', 
                    protocol = '', 
                    skip_beneficiary_data_validation = True, 
                    travel_rule_behavior = True, 
                    originator_proof = null, 
                    beneficiary_proof = null, 
                    pii = null, ),
                auto_staking = True,
                network_staking = None,
                cpu_staking = None,
                use_gasless = True
            )
        else:
            return TransactionRequest(
        )
        """

    def testTransactionRequest(self):
        """Test TransactionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
