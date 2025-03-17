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

from fireblocks.models.create_token_request_dto_create_params import (
    CreateTokenRequestDtoCreateParams,
)


class TestCreateTokenRequestDtoCreateParams(unittest.TestCase):
    """CreateTokenRequestDtoCreateParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTokenRequestDtoCreateParams:
        """Test CreateTokenRequestDtoCreateParams
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateTokenRequestDtoCreateParams`
        """
        model = CreateTokenRequestDtoCreateParams()
        if include_optional:
            return CreateTokenRequestDtoCreateParams(
                contract_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d',
                deploy_function_params = [{internalType=string, name=name, type=string, value=name}, {internalType=string, name=symbol, type=string, value=symbol}, {components=[{internalType=bool, name=_isMintable, type=bool}], internalType=struct MyStruct, name=customConfigProps, type=tuple, value=[{internalType=bool, name=_isMintable, type=bool, value=false}]}],
                symbol = 'MyUSDT',
                name = 'My USD Tether',
                issuer_address = 'rnDV4JiwgRNhudPY2sm65AzECpRXaasL4r'
            )
        else:
            return CreateTokenRequestDtoCreateParams(
                contract_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d',
                symbol = 'MyUSDT',
                name = 'My USD Tether',
                issuer_address = 'rnDV4JiwgRNhudPY2sm65AzECpRXaasL4r',
        )
        """

    def testCreateTokenRequestDtoCreateParams(self):
        """Test CreateTokenRequestDtoCreateParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
