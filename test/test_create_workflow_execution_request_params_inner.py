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

from fireblocks.models.create_workflow_execution_request_params_inner import (
    CreateWorkflowExecutionRequestParamsInner,
)


class TestCreateWorkflowExecutionRequestParamsInner(unittest.TestCase):
    """CreateWorkflowExecutionRequestParamsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> CreateWorkflowExecutionRequestParamsInner:
        """Test CreateWorkflowExecutionRequestParamsInner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateWorkflowExecutionRequestParamsInner`
        """
        model = CreateWorkflowExecutionRequestParamsInner()
        if include_optional:
            return CreateWorkflowExecutionRequestParamsInner(
                config_operation_id = '',
                execution_params = fireblocks.models.disbursement_operation_execution_params_execution_params.DisbursementOperationExecutionParams_executionParams(
                    amount = '', 
                    payment_account = fireblocks.models.account.Account(
                        account_id = '', 
                        account_type = 'EXCHANGE_ACCOUNT', ), 
                    instruction_set = [
                        null
                        ], )
            )
        else:
            return CreateWorkflowExecutionRequestParamsInner(
                config_operation_id = '',
        )
        """

    def testCreateWorkflowExecutionRequestParamsInner(self):
        """Test CreateWorkflowExecutionRequestParamsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
