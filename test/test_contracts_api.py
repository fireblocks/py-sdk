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

from fireblocks.api.contracts_api import ContractsApi


class TestContractsApi(unittest.TestCase):
    """ContractsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContractsApi()

    def tearDown(self) -> None:
        pass

    def test_add_contract_asset(self) -> None:
        """Test case for add_contract_asset

        Add an asset to a contract
        """
        pass

    def test_create_contract(self) -> None:
        """Test case for create_contract

        Create a contract
        """
        pass

    def test_delete_contract(self) -> None:
        """Test case for delete_contract

        Delete a contract
        """
        pass

    def test_delete_contract_asset(self) -> None:
        """Test case for delete_contract_asset

        Delete a contract asset
        """
        pass

    def test_get_contract(self) -> None:
        """Test case for get_contract

        Find a specific contract
        """
        pass

    def test_get_contract_asset(self) -> None:
        """Test case for get_contract_asset

        Find a contract asset
        """
        pass

    def test_get_contracts(self) -> None:
        """Test case for get_contracts

        List contracts
        """
        pass


if __name__ == "__main__":
    unittest.main()
