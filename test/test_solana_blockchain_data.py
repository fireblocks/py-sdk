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

from fireblocks.models.solana_blockchain_data import SolanaBlockchainData


class TestSolanaBlockchainData(unittest.TestCase):
    """SolanaBlockchainData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SolanaBlockchainData:
        """Test SolanaBlockchainData
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SolanaBlockchainData`
        """
        model = SolanaBlockchainData()
        if include_optional:
            return SolanaBlockchainData(
                stake_account_address = '3Ru67FyzMTcdENmmRL4Eve4dtPd6AdpuypR21q5EQCdq',
                stake_account_derivation_change_value = 7
            )
        else:
            return SolanaBlockchainData(
                stake_account_address = '3Ru67FyzMTcdENmmRL4Eve4dtPd6AdpuypR21q5EQCdq',
                stake_account_derivation_change_value = 7,
        )
        """

    def testSolanaBlockchainData(self):
        """Test SolanaBlockchainData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
