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

from fireblocks.models.screening_policy_response import ScreeningPolicyResponse


class TestScreeningPolicyResponse(unittest.TestCase):
    """ScreeningPolicyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScreeningPolicyResponse:
        """Test ScreeningPolicyResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ScreeningPolicyResponse`
        """
        model = ScreeningPolicyResponse()
        if include_optional:
            return ScreeningPolicyResponse(
                policy = fireblocks.models.travel_rule_policy_rule_response.TravelRulePolicyRuleResponse(
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
                    action = 'SCREEN', ),
                policy_status = '',
                is_default = True,
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ScreeningPolicyResponse(
                policy = fireblocks.models.travel_rule_policy_rule_response.TravelRulePolicyRuleResponse(
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
                    action = 'SCREEN', ),
                is_default = True,
                last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testScreeningPolicyResponse(self):
        """Test ScreeningPolicyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
