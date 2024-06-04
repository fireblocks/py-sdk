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

from fireblocks.models.solana_blockchain_data_dto import SolanaBlockchainDataDto


class TestSolanaBlockchainDataDto(unittest.TestCase):
    """SolanaBlockchainDataDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SolanaBlockchainDataDto:
        """Test SolanaBlockchainDataDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SolanaBlockchainDataDto`
        """
        model = SolanaBlockchainDataDto()
        if include_optional:
            return SolanaBlockchainDataDto(
                stake_account_address = '3Ru67FyzMTcdENmmRL4Eve4dtPd6AdpuypR21q5EQCdq'
            )
        else:
            return SolanaBlockchainDataDto(
                stake_account_address = '3Ru67FyzMTcdENmmRL4Eve4dtPd6AdpuypR21q5EQCdq',
        )
        """

    def testSolanaBlockchainDataDto(self):
        """Test SolanaBlockchainDataDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()