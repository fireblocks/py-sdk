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

from fireblocks_client.models.read_abi_function import ReadAbiFunction


class TestReadAbiFunction(unittest.TestCase):
    """ReadAbiFunction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadAbiFunction:
        """Test ReadAbiFunction
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ReadAbiFunction`
        """
        model = ReadAbiFunction()
        if include_optional:
            return ReadAbiFunction(
                state_mutability = 'pure',
                outputs = [
                    fireblocks_client.models.parameter.Parameter(
                        name = '_name', 
                        description = 'The name of the token', 
                        internal_type = 'string', 
                        type = 'string', 
                        components = [
                            fireblocks_client.models.parameter.Parameter(
                                name = '_name', 
                                description = 'The name of the token', 
                                internal_type = 'string', 
                                type = 'string', )
                            ], )
                    ],
                name = '',
                type = '',
                inputs = [
                    fireblocks_client.models.parameter_with_value.ParameterWithValue(
                        name = '_name', 
                        description = 'The name of the token', 
                        internal_type = 'string', 
                        type = 'string', 
                        components = [
                            fireblocks_client.models.parameter.Parameter(
                                name = '_name', 
                                description = 'The name of the token', 
                                internal_type = 'string', 
                                type = 'string', )
                            ], 
                        value = 'true', 
                        function_value = null, )
                    ],
                description = ''
            )
        else:
            return ReadAbiFunction(
                state_mutability = 'pure',
                type = '',
                inputs = [
                    fireblocks_client.models.parameter_with_value.ParameterWithValue(
                        name = '_name', 
                        description = 'The name of the token', 
                        internal_type = 'string', 
                        type = 'string', 
                        components = [
                            fireblocks_client.models.parameter.Parameter(
                                name = '_name', 
                                description = 'The name of the token', 
                                internal_type = 'string', 
                                type = 'string', )
                            ], 
                        value = 'true', 
                        function_value = null, )
                    ],
        )
        """

    def testReadAbiFunction(self):
        """Test ReadAbiFunction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
