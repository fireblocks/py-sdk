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

from fireblocks.models.remove_collateral_request_body import RemoveCollateralRequestBody


class TestRemoveCollateralRequestBody(unittest.TestCase):
    """RemoveCollateralRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoveCollateralRequestBody:
        """Test RemoveCollateralRequestBody
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RemoveCollateralRequestBody`
        """
        model = RemoveCollateralRequestBody()
        if include_optional:
            return RemoveCollateralRequestBody(
                transaction_request = fireblocks.models.transaction_request.TransactionRequest(
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
                        id = '', 
                        name = '', 
                        wallet_id = '', 
                        one_time_address = fireblocks.models.one_time_address.OneTimeAddress(
                            address = '', 
                            tag = '', ), ), 
                    destinations = [
                        fireblocks.models.transaction_request_destination.TransactionRequestDestination(
                            amount = '', )
                        ], 
                    amount = null, 
                    treat_as_gross_amount = False, 
                    force_sweep = False, 
                    fee_level = 'MEDIUM', 
                    fee = null, 
                    priority_fee = null, 
                    fail_on_low_fee = True, 
                    max_fee = '120', 
                    max_total_fee = '88', 
                    gas_limit = null, 
                    gas_price = null, 
                    network_fee = null, 
                    replace_tx_by_hash = '00000000-0000-0000-0000-000000000000', 
                    extra_parameters = fireblocks.models.extra_parameters.extraParameters(), 
                    customer_ref_id = 'abcdef', 
                    travel_rule_message = fireblocks.models.travel_rule_create_transaction_request.TravelRuleCreateTransactionRequest(
                        originator_vas_pdid = '', 
                        beneficiary_vas_pdid = '', 
                        originator_vas_pname = '', 
                        beneficiary_vas_pname = '', 
                        transaction_blockchain_info = null, 
                        originator = null, 
                        beneficiary = null, 
                        encrypted = '', 
                        protocol = '', 
                        skip_beneficiary_data_validation = True, 
                        travel_rule_behavior = True, 
                        originator_ref = '', 
                        beneficiary_ref = '', 
                        travel_rule_behavior_ref = '', 
                        originator_proof = null, 
                        beneficiary_proof = null, 
                        beneficiary_did = '', 
                        originator_did = '', 
                        is_non_custodial = True, ), 
                    auto_staking = True, 
                    network_staking = null, 
                    cpu_staking = null, 
                    use_gasless = True, ),
                is_dst_collateral = True
            )
        else:
            return RemoveCollateralRequestBody(
        )
        """

    def testRemoveCollateralRequestBody(self):
        """Test RemoveCollateralRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
