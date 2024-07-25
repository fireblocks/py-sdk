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

from fireblocks.models.read_call_function_dto import ReadCallFunctionDto


class TestReadCallFunctionDto(unittest.TestCase):
    """ReadCallFunctionDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadCallFunctionDto:
        """Test ReadCallFunctionDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ReadCallFunctionDto`
        """
        model = ReadCallFunctionDto()
        if include_optional:
            return ReadCallFunctionDto(
                abi_function = fireblocks.models.read_abi_function.ReadAbiFunction(
                    state_mutability = 'pure', 
                    outputs = [
                        fireblocks.models.parameter.Parameter(
                            name = '_name', 
                            description = 'The name of the token', 
                            internal_type = 'string', 
                            type = 'string', 
                            components = [
                                fireblocks.models.parameter.Parameter(
                                    name = '_name', 
                                    description = 'The name of the token', 
                                    internal_type = 'string', 
                                    type = 'string', )
                                ], )
                        ], 
                    name = '', 
                    type = '', 
                    inputs = [
                        fireblocks.models.parameter_with_value.ParameterWithValue(
                            name = '_name', 
                            description = 'The name of the token', 
                            internal_type = 'string', 
                            type = 'string', 
                            value = 'true', 
                            function_value = null, )
                        ], 
                    description = '', )
            )
        else:
            return ReadCallFunctionDto(
                abi_function = fireblocks.models.read_abi_function.ReadAbiFunction(
                    state_mutability = 'pure', 
                    outputs = [
                        fireblocks.models.parameter.Parameter(
                            name = '_name', 
                            description = 'The name of the token', 
                            internal_type = 'string', 
                            type = 'string', 
                            components = [
                                fireblocks.models.parameter.Parameter(
                                    name = '_name', 
                                    description = 'The name of the token', 
                                    internal_type = 'string', 
                                    type = 'string', )
                                ], )
                        ], 
                    name = '', 
                    type = '', 
                    inputs = [
                        fireblocks.models.parameter_with_value.ParameterWithValue(
                            name = '_name', 
                            description = 'The name of the token', 
                            internal_type = 'string', 
                            type = 'string', 
                            value = 'true', 
                            function_value = null, )
                        ], 
                    description = '', ),
        )
        """

    def testReadCallFunctionDto(self):
        """Test ReadCallFunctionDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
