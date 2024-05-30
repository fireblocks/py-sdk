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

from fireblocks.models.screening_operation_execution_output import (
    ScreeningOperationExecutionOutput,
)


class TestScreeningOperationExecutionOutput(unittest.TestCase):
    """ScreeningOperationExecutionOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScreeningOperationExecutionOutput:
        """Test ScreeningOperationExecutionOutput
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ScreeningOperationExecutionOutput`
        """
        model = ScreeningOperationExecutionOutput()
        if include_optional:
            return ScreeningOperationExecutionOutput(
                verdicts = [
                    fireblocks.models.screening_verdict.ScreeningVerdict(
                        verdict = 'PASSED', 
                        execution_operation_id = '', 
                        account = null, 
                        asset_id = '', 
                        amount = '', 
                        matched_rule = fireblocks.models.screening_verdict_matched_rule.ScreeningVerdict_matchedRule(
                            action = '', 
                            category = [
                                ''
                                ], ), )
                    ]
            )
        else:
            return ScreeningOperationExecutionOutput(
                verdicts = [
                    fireblocks.models.screening_verdict.ScreeningVerdict(
                        verdict = 'PASSED', 
                        execution_operation_id = '', 
                        account = null, 
                        asset_id = '', 
                        amount = '', 
                        matched_rule = fireblocks.models.screening_verdict_matched_rule.ScreeningVerdict_matchedRule(
                            action = '', 
                            category = [
                                ''
                                ], ), )
                    ],
        )
        """

    def testScreeningOperationExecutionOutput(self):
        """Test ScreeningOperationExecutionOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
