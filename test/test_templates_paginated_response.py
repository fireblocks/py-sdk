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

from fireblocks_client.models.templates_paginated_response import (
    TemplatesPaginatedResponse,
)


class TestTemplatesPaginatedResponse(unittest.TestCase):
    """TemplatesPaginatedResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemplatesPaginatedResponse:
        """Test TemplatesPaginatedResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TemplatesPaginatedResponse`
        """
        model = TemplatesPaginatedResponse()
        if include_optional:
            return TemplatesPaginatedResponse(
                data = [
                    fireblocks_client.models.lean_contract_dto.LeanContractDto(
                        id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d', 
                        name = 'My Contract', 
                        description = 'an ERC20 implementation', 
                        attributes = {"useCases":["Stablecoin","CBDC"],"standards":["ERC-20","ERC-1400"],"auditor":{"name":"MyAuditor","imageURL":"https://my-images.com/my-image.jpg","link":"https://my-auditor.com/my-audit-report"}}, 
                        is_public = True, 
                        can_deploy = True, 
                        owner = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d', 
                        vendor = null, 
                        type = 'FUNGIBLE_TOKEN', )
                    ],
                next = 'eJ0eXAiOiJKV1QiLCJhbGcOiJIUzI1NiJ9'
            )
        else:
            return TemplatesPaginatedResponse(
                data = [
                    fireblocks_client.models.lean_contract_dto.LeanContractDto(
                        id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d', 
                        name = 'My Contract', 
                        description = 'an ERC20 implementation', 
                        attributes = {"useCases":["Stablecoin","CBDC"],"standards":["ERC-20","ERC-1400"],"auditor":{"name":"MyAuditor","imageURL":"https://my-images.com/my-image.jpg","link":"https://my-auditor.com/my-audit-report"}}, 
                        is_public = True, 
                        can_deploy = True, 
                        owner = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d', 
                        vendor = null, 
                        type = 'FUNGIBLE_TOKEN', )
                    ],
        )
        """

    def testTemplatesPaginatedResponse(self):
        """Test TemplatesPaginatedResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
