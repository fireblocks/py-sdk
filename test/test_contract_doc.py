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

from fireblocks.models.contract_doc import ContractDoc


class TestContractDoc(unittest.TestCase):
    """ContractDoc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractDoc:
        """Test ContractDoc
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ContractDoc`
        """
        model = ContractDoc()
        if include_optional:
            return ContractDoc(
                details = 'A token that can be minted and burned',
                events = 'Upgraded(address): {"details": "Emitted when the implementation is upgraded."}',
                kind = 'dev',
                methods = {"constructor":{"details":"Initializes the contract"}},
                version = '1'
            )
        else:
            return ContractDoc(
                kind = 'dev',
                methods = {"constructor":{"details":"Initializes the contract"}},
                version = '1',
        )
        """

    def testContractDoc(self):
        """Test ContractDoc"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
