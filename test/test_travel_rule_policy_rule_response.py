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

from fireblocks.models.travel_rule_policy_rule_response import (
    TravelRulePolicyRuleResponse,
)


class TestTravelRulePolicyRuleResponse(unittest.TestCase):
    """TravelRulePolicyRuleResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRulePolicyRuleResponse:
        """Test TravelRulePolicyRuleResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRulePolicyRuleResponse`
        """
        model = TravelRulePolicyRuleResponse()
        if include_optional:
            return TravelRulePolicyRuleResponse(
                source_type = '',
                source_sub_type = '',
                dest_type = '',
                dest_sub_type = '',
                dest_address = '',
                source_id = '',
                dest_id = '',
                asset = '',
                base_asset = '',
                amount = 1.337,
                amount_usd = 1.337,
                network_protocol = '',
                operation = '',
                action = 'SCREEN'
            )
        else:
            return TravelRulePolicyRuleResponse(
                action = 'SCREEN',
        )
        """

    def testTravelRulePolicyRuleResponse(self):
        """Test TravelRulePolicyRuleResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
