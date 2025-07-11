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

from fireblocks.models.policy_rule_check_result import PolicyRuleCheckResult


class TestPolicyRuleCheckResult(unittest.TestCase):
    """PolicyRuleCheckResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicyRuleCheckResult:
        """Test PolicyRuleCheckResult
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PolicyRuleCheckResult`
        """
        model = PolicyRuleCheckResult()
        if include_optional:
            return PolicyRuleCheckResult(
                index = 1.337,
                status = 'ok',
                errors = [
                    fireblocks.models.policy_rule_error.PolicyRuleError(
                        error_message = '', 
                        error_code = 1.337, 
                        error_code_name = '', 
                        error_field = 'operator', )
                    ]
            )
        else:
            return PolicyRuleCheckResult(
                index = 1.337,
                status = 'ok',
                errors = [
                    fireblocks.models.policy_rule_error.PolicyRuleError(
                        error_message = '', 
                        error_code = 1.337, 
                        error_code_name = '', 
                        error_field = 'operator', )
                    ],
        )
        """

    def testPolicyRuleCheckResult(self):
        """Test PolicyRuleCheckResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
