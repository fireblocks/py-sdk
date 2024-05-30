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

from fireblocks_client.api.contract_templates_api import ContractTemplatesApi


class TestContractTemplatesApi(unittest.TestCase):
    """ContractTemplatesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContractTemplatesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_contract_template_by_id(self) -> None:
        """Test case for delete_contract_template_by_id

        Delete a contract template by id
        """
        pass

    def test_deploy_contract(self) -> None:
        """Test case for deploy_contract

        Deploy contract
        """
        pass

    def test_get_constructor_by_contract_template_id(self) -> None:
        """Test case for get_constructor_by_contract_template_id

        Return contract template's constructor
        """
        pass

    def test_get_contract_template_by_id(self) -> None:
        """Test case for get_contract_template_by_id

        Return contract template by id
        """
        pass

    def test_get_contract_templates(self) -> None:
        """Test case for get_contract_templates

        List all contract templates
        """
        pass

    def test_get_function_abi_by_contract_template_id(self) -> None:
        """Test case for get_function_abi_by_contract_template_id

        Return contract template's function
        """
        pass

    def test_upload_contract_template(self) -> None:
        """Test case for upload_contract_template

        Upload contract template
        """
        pass


if __name__ == "__main__":
    unittest.main()
