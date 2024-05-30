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

from fireblocks_client.models.contract_metadata_dto import ContractMetadataDto


class TestContractMetadataDto(unittest.TestCase):
    """ContractMetadataDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractMetadataDto:
        """Test ContractMetadataDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ContractMetadataDto`
        """
        model = ContractMetadataDto()
        if include_optional:
            return ContractMetadataDto(
                id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb',
                blockchain_id = 'B7QG017M',
                contract_address = '0x1234567890abcdef1234567890abcdef12345678',
                contract_template_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d',
                vault_account_id = '0'
            )
        else:
            return ContractMetadataDto(
                id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb',
                blockchain_id = 'B7QG017M',
                contract_address = '0x1234567890abcdef1234567890abcdef12345678',
                contract_template_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d',
        )
        """

    def testContractMetadataDto(self):
        """Test ContractMetadataDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
