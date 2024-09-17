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

from fireblocks.models.contract_with_abi_dto import ContractWithAbiDto


class TestContractWithAbiDto(unittest.TestCase):
    """ContractWithAbiDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractWithAbiDto:
        """Test ContractWithAbiDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ContractWithAbiDto`
        """
        model = ContractWithAbiDto()
        if include_optional:
            return ContractWithAbiDto(
                contract_address = '0xfff9976782d46cc05630d1f6ebab18b2324d6b14',
                base_asset_id = 'ETH_TEST6',
                name = 'WETH9',
                abi = [{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"nonpayable","type":"function","name":"mint"}],
                is_proxy = True,
                implementation = '0xfff9976782d46cc05630d1f6ebab18b2324d6b14',
                is_public = True
            )
        else:
            return ContractWithAbiDto(
                contract_address = '0xfff9976782d46cc05630d1f6ebab18b2324d6b14',
                base_asset_id = 'ETH_TEST6',
                name = 'WETH9',
                abi = [{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"nonpayable","type":"function","name":"mint"}],
                is_public = True,
        )
        """

    def testContractWithAbiDto(self):
        """Test ContractWithAbiDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()