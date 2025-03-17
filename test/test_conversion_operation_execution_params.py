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

from fireblocks.models.conversion_operation_execution_params import (
    ConversionOperationExecutionParams,
)


class TestConversionOperationExecutionParams(unittest.TestCase):
    """ConversionOperationExecutionParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConversionOperationExecutionParams:
        """Test ConversionOperationExecutionParams
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ConversionOperationExecutionParams`
        """
        model = ConversionOperationExecutionParams()
        if include_optional:
            return ConversionOperationExecutionParams(
                config_operation_id = '',
                execution_params = fireblocks.models.conversion_operation_execution_params_execution_params.ConversionOperationExecutionParams_executionParams(
                    amount = '', 
                    account_id = '', 
                    src_asset_id = '', 
                    dest_asset_id = '', 
                    slippage_basis_points = 0, )
            )
        else:
            return ConversionOperationExecutionParams(
                config_operation_id = '',
        )
        """

    def testConversionOperationExecutionParams(self):
        """Test ConversionOperationExecutionParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
