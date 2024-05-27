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

from fireblocks_client.api.deployed_contracts_api import DeployedContractsApi


class TestDeployedContractsApi(unittest.TestCase):
    """DeployedContractsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DeployedContractsApi()

    def tearDown(self) -> None:
        pass

    def test_get_deployed_contract_by_address(self) -> None:
        """Test case for get_deployed_contract_by_address

        Return deployed contract data
        """
        pass

    def test_get_deployed_contract_by_id(self) -> None:
        """Test case for get_deployed_contract_by_id

        Return deployed contract data by id
        """
        pass

    def test_get_deployed_contracts(self) -> None:
        """Test case for get_deployed_contracts

        List deployed contracts data
        """
        pass


if __name__ == "__main__":
    unittest.main()
