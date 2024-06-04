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

from fireblocks.models.transaction_response import TransactionResponse


class TestTransactionResponse(unittest.TestCase):
    """TransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionResponse:
        """Test TransactionResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TransactionResponse`
        """
        model = TransactionResponse()
        if include_optional:
            return TransactionResponse(
                id = '',
                external_tx_id = '',
                status = '',
                sub_status = '',
                tx_hash = '',
                operation = 'TRANSFER',
                note = '',
                asset_id = '',
                source = fireblocks.models.source_transfer_peer_path_response.SourceTransferPeerPathResponse(
                    type = 'VAULT_ACCOUNT', 
                    sub_type = '', 
                    id = '', 
                    name = '', 
                    wallet_id = '', ),
                source_address = '',
                tag = '',
                destination = fireblocks.models.destination_transfer_peer_path_response.DestinationTransferPeerPathResponse(
                    type = 'VAULT_ACCOUNT', 
                    sub_type = '', 
                    id = '', 
                    name = '', 
                    wallet_id = '', ),
                destinations = [
                    fireblocks.models.transaction_response_destination.TransactionResponseDestination(
                        destination_address = null, 
                        destination_address_description = null, 
                        amount = '', 
                        amount_usd = '', 
                        aml_screening_result = fireblocks.models.aml_screening_result.AmlScreeningResult(
                            provider = '', 
                            payload = fireblocks.models.payload.payload(), ), 
                        destination = fireblocks.models.destination_transfer_peer_path_response.DestinationTransferPeerPathResponse(
                            type = 'VAULT_ACCOUNT', 
                            sub_type = '', 
                            id = '', 
                            name = '', 
                            wallet_id = '', ), 
                        authorization_info = fireblocks.models.authorization_info.AuthorizationInfo(
                            allow_operator_as_authorizer = True, 
                            logic = 'AND', 
                            groups = [
                                fireblocks.models.authorization_groups.AuthorizationGroups(
                                    th = 1.337, 
                                    users = {
                                        'PENDING_AUTHORIZATION' : 'PENDING_AUTHORIZATION'
                                        }, )
                                ], ), )
                    ],
                destination_address = '',
                destination_address_description = '',
                destination_tag = '',
                contract_call_decoded_data = fireblocks.models.transaction_response_contract_call_decoded_data.TransactionResponse_contractCallDecodedData(
                    contract_name = '', 
                    function_calls = [
                        None
                        ], ),
                amount_info = fireblocks.models.amount_info.AmountInfo(
                    amount = '', 
                    requested_amount = '', 
                    net_amount = '', 
                    amount_usd = '', ),
                treat_as_gross_amount = True,
                fee_info = fireblocks.models.fee_info.FeeInfo(
                    network_fee = '', 
                    service_fee = '', 
                    gas_price = '', ),
                fee_currency = '',
                network_records = [
                    fireblocks.models.network_record.NetworkRecord(
                        source = fireblocks.models.source_transfer_peer_path_response.SourceTransferPeerPathResponse(
                            type = 'VAULT_ACCOUNT', 
                            sub_type = '', 
                            id = '', 
                            name = '', 
                            wallet_id = '', ), 
                        destination = fireblocks.models.destination_transfer_peer_path_response.DestinationTransferPeerPathResponse(
                            type = 'VAULT_ACCOUNT', 
                            sub_type = '', 
                            id = '', 
                            name = '', 
                            wallet_id = '', ), 
                        tx_hash = '', 
                        network_fee = '', 
                        asset_id = '', 
                        net_amount = '', 
                        is_dropped = True, 
                        type = '', 
                        destination_address = '', 
                        source_address = '', 
                        amount_usd = '', 
                        index = 1.337, 
                        reward_info = fireblocks.models.reward_info.RewardInfo(
                            src_rewards = '', 
                            dest_rewards = '', ), )
                    ],
                created_at = 1.337,
                last_updated = 1.337,
                created_by = '',
                signed_by = [
                    ''
                    ],
                rejected_by = '',
                authorization_info = fireblocks.models.authorization_info.AuthorizationInfo(
                    allow_operator_as_authorizer = True, 
                    logic = 'AND', 
                    groups = [
                        fireblocks.models.authorization_groups.AuthorizationGroups(
                            th = 1.337, 
                            users = {
                                'PENDING_AUTHORIZATION' : 'PENDING_AUTHORIZATION'
                                }, )
                        ], ),
                exchange_tx_id = '',
                customer_ref_id = '',
                aml_screening_result = fireblocks.models.aml_screening_result.AmlScreeningResult(
                    provider = '', 
                    payload = fireblocks.models.payload.payload(), ),
                compliance_result = fireblocks.models.compliance_result.ComplianceResult(
                    aml = [
                        fireblocks.models.compliance_screening_result.ComplianceScreeningResult(
                            provider = '', 
                            payload = fireblocks.models.payload.payload(), 
                            bypass_reason = '', 
                            screening_status = 'COMPLETED', 
                            timestamp = 1.337, )
                        ], 
                    tr = [
                        fireblocks.models.compliance_screening_result.ComplianceScreeningResult(
                            provider = '', 
                            payload = fireblocks.models.payload.payload(), 
                            bypass_reason = '', 
                            screening_status = 'COMPLETED', 
                            timestamp = 1.337, )
                        ], 
                    aml_list = [
                        
                        ], 
                    status = 'Started', 
                    aml_registration = [
                        fireblocks.models.aml_registration_result.AmlRegistrationResult(
                            provider = '', 
                            success = True, 
                            timestamp = 1.337, )
                        ], ),
                extra_parameters = None,
                signed_messages = [
                    fireblocks.models.signed_message.SignedMessage(
                        content = '', 
                        algorithm = 'MPC_ECDSA_SECP256K1', 
                        derivation_path = [
                            1.337
                            ], 
                        signature = fireblocks.models.signed_message_signature.SignedMessage_signature(
                            full_sig = '', 
                            r = '', 
                            s = '', 
                            v = 1.337, ), 
                        public_key = '', )
                    ],
                num_of_confirmations = 1.337,
                block_info = fireblocks.models.block_info.BlockInfo(
                    block_height = '', 
                    block_hash = '', ),
                index = 1.337,
                reward_info = fireblocks.models.reward_info.RewardInfo(
                    src_rewards = '', 
                    dest_rewards = '', ),
                system_messages = fireblocks.models.system_message_info.SystemMessageInfo(
                    type = 'WARN', 
                    message = 'Slow transaction processing. Outgoing transactions might be stuck.', ),
                address_type = '',
                requested_amount = 1.337,
                amount = 1.337,
                net_amount = 1.337,
                amount_usd = 1.337,
                service_fee = 1.337,
                fee = 1.337,
                network_fee = 1.337,
                error_description = ''
            )
        else:
            return TransactionResponse(
        )
        """

    def testTransactionResponse(self):
        """Test TransactionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()