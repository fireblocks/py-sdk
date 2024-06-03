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

from fireblocks.models.policy_and_validation_response import PolicyAndValidationResponse


class TestPolicyAndValidationResponse(unittest.TestCase):
    """PolicyAndValidationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicyAndValidationResponse:
        """Test PolicyAndValidationResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PolicyAndValidationResponse`
        """
        model = PolicyAndValidationResponse()
        if include_optional:
            return PolicyAndValidationResponse(
                policy = fireblocks.models.policy_response.PolicyResponse(
                    rules = [
                        fireblocks.models.policy_rule.PolicyRule(
                            operator = '', 
                            operators = fireblocks.models.policy_rule_operators.PolicyRule_operators(
                                wildcard = '*', 
                                users = [
                                    ''
                                    ], 
                                users_groups = [
                                    ''
                                    ], 
                                services = [
                                    ''
                                    ], ), 
                            transaction_type = 'TRANSFER', 
                            designated_signer = '', 
                            designated_signers = fireblocks.models.policy_rule_designated_signers.PolicyRule_designatedSigners(), 
                            type = 'TRANSFER', 
                            action = 'ALLOW', 
                            asset = '', 
                            src_type = null, 
                            src_sub_type = null, 
                            src_id = null, 
                            src = fireblocks.models.policy_rule_src.PolicyRule_src(
                                ids = [
                                    [
                                        null
                                        ]
                                    ], ), 
                            dst_type = null, 
                            dst_sub_type = null, 
                            dst_id = null, 
                            dst = fireblocks.models.policy_rule_dst.PolicyRule_dst(), 
                            dst_address_type = 'WHITELISTED', 
                            amount_currency = 'USD', 
                            amount_scope = 'SINGLE_TX', 
                            amount = null, 
                            period_sec = 1.337, 
                            authorizers = [
                                ''
                                ], 
                            authorizers_count = 1.337, 
                            authorization_groups = fireblocks.models.policy_rule_authorization_groups.PolicyRule_authorizationGroups(
                                logic = 'AND', 
                                allow_operator_as_authorizer = True, 
                                groups = [
                                    fireblocks.models.policy_rule_authorization_groups_groups_inner.PolicyRule_authorizationGroups_groups_inner(
                                        th = 1.337, )
                                    ], ), 
                            amount_aggregation = fireblocks.models.policy_rule_amount_aggregation.PolicyRule_amountAggregation(
                                src_transfer_peers = 'PER_SINGLE_MATCH', 
                                dst_transfer_peers = 'PER_SINGLE_MATCH', ), 
                            raw_message_signing = fireblocks.models.policy_rule_raw_message_signing.PolicyRule_rawMessageSigning(
                                algorithm = '', 
                                derivation_path = fireblocks.models.policy_rule_raw_message_signing_derivation_path.PolicyRule_rawMessageSigning_derivationPath(
                                    path = [
                                        1.337
                                        ], ), ), 
                            apply_for_approve = True, 
                            apply_for_typed_message = True, 
                            external_descriptor = '', )
                        ], 
                    metadata = fireblocks.models.policy_metadata.PolicyMetadata(
                        edited_by = '', 
                        edited_at = '', 
                        published_by = '', 
                        published_at = '', ), ),
                validation = fireblocks.models.policy_validation.PolicyValidation(
                    status = '', 
                    check_result = fireblocks.models.policy_check_result.PolicyCheckResult(
                        errors = 1.337, 
                        results = [
                            fireblocks.models.policy_rule_check_result.PolicyRuleCheckResult(
                                index = 1.337, 
                                status = 'ok', 
                                errors = [
                                    fireblocks.models.policy_rule_error.PolicyRuleError(
                                        error_message = '', 
                                        error_code = 1.337, 
                                        error_code_name = '', 
                                        error_field = 'operator', )
                                    ], )
                            ], ), )
            )
        else:
            return PolicyAndValidationResponse(
                policy = fireblocks.models.policy_response.PolicyResponse(
                    rules = [
                        fireblocks.models.policy_rule.PolicyRule(
                            operator = '', 
                            operators = fireblocks.models.policy_rule_operators.PolicyRule_operators(
                                wildcard = '*', 
                                users = [
                                    ''
                                    ], 
                                users_groups = [
                                    ''
                                    ], 
                                services = [
                                    ''
                                    ], ), 
                            transaction_type = 'TRANSFER', 
                            designated_signer = '', 
                            designated_signers = fireblocks.models.policy_rule_designated_signers.PolicyRule_designatedSigners(), 
                            type = 'TRANSFER', 
                            action = 'ALLOW', 
                            asset = '', 
                            src_type = null, 
                            src_sub_type = null, 
                            src_id = null, 
                            src = fireblocks.models.policy_rule_src.PolicyRule_src(
                                ids = [
                                    [
                                        null
                                        ]
                                    ], ), 
                            dst_type = null, 
                            dst_sub_type = null, 
                            dst_id = null, 
                            dst = fireblocks.models.policy_rule_dst.PolicyRule_dst(), 
                            dst_address_type = 'WHITELISTED', 
                            amount_currency = 'USD', 
                            amount_scope = 'SINGLE_TX', 
                            amount = null, 
                            period_sec = 1.337, 
                            authorizers = [
                                ''
                                ], 
                            authorizers_count = 1.337, 
                            authorization_groups = fireblocks.models.policy_rule_authorization_groups.PolicyRule_authorizationGroups(
                                logic = 'AND', 
                                allow_operator_as_authorizer = True, 
                                groups = [
                                    fireblocks.models.policy_rule_authorization_groups_groups_inner.PolicyRule_authorizationGroups_groups_inner(
                                        th = 1.337, )
                                    ], ), 
                            amount_aggregation = fireblocks.models.policy_rule_amount_aggregation.PolicyRule_amountAggregation(
                                src_transfer_peers = 'PER_SINGLE_MATCH', 
                                dst_transfer_peers = 'PER_SINGLE_MATCH', ), 
                            raw_message_signing = fireblocks.models.policy_rule_raw_message_signing.PolicyRule_rawMessageSigning(
                                algorithm = '', 
                                derivation_path = fireblocks.models.policy_rule_raw_message_signing_derivation_path.PolicyRule_rawMessageSigning_derivationPath(
                                    path = [
                                        1.337
                                        ], ), ), 
                            apply_for_approve = True, 
                            apply_for_typed_message = True, 
                            external_descriptor = '', )
                        ], 
                    metadata = fireblocks.models.policy_metadata.PolicyMetadata(
                        edited_by = '', 
                        edited_at = '', 
                        published_by = '', 
                        published_at = '', ), ),
                validation = fireblocks.models.policy_validation.PolicyValidation(
                    status = '', 
                    check_result = fireblocks.models.policy_check_result.PolicyCheckResult(
                        errors = 1.337, 
                        results = [
                            fireblocks.models.policy_rule_check_result.PolicyRuleCheckResult(
                                index = 1.337, 
                                status = 'ok', 
                                errors = [
                                    fireblocks.models.policy_rule_error.PolicyRuleError(
                                        error_message = '', 
                                        error_code = 1.337, 
                                        error_code_name = '', 
                                        error_field = 'operator', )
                                    ], )
                            ], ), ),
        )
        """

    def testPolicyAndValidationResponse(self):
        """Test PolicyAndValidationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
