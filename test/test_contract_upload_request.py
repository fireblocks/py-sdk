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

from fireblocks.models.contract_upload_request import ContractUploadRequest


class TestContractUploadRequest(unittest.TestCase):
    """ContractUploadRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractUploadRequest:
        """Test ContractUploadRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ContractUploadRequest`
        """
        model = ContractUploadRequest()
        if include_optional:
            return ContractUploadRequest(
                name = 'My Contract',
                description = 'an ERC20 implementation',
                long_description = 'a full ERC20 implementation, containing the following:

 - mint
 - burn
',
                bytecode = '',
                sourcecode = '',
                type = 'FUNGIBLE_TOKEN',
                docs = fireblocks.models.contract_doc.ContractDoc(
                    details = 'A token that can be minted and burned', 
                    events = 'Upgraded(address): {"details": "Emitted when the implementation is upgraded."}', 
                    kind = 'dev', 
                    methods = {"constructor":{"details":"Initializes the contract"}}, 
                    version = 1, ),
                abi = [{"inputs":[{"internalType":"address","name":"implementation","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"stateMutability":"payable","type":"constructor"}],
                attributes = fireblocks.models.contract_attributes.ContractAttributes(
                    use_cases = [
                        ''
                        ], 
                    standards = [
                        ''
                        ], 
                    auditor = fireblocks.models.auditor_data.AuditorData(
                        name = '', 
                        image_url = '', 
                        link = '', ), ),
                protocol = 'ETH'
            )
        else:
            return ContractUploadRequest(
                name = 'My Contract',
                description = 'an ERC20 implementation',
                bytecode = '',
                type = 'FUNGIBLE_TOKEN',
                abi = [{"inputs":[{"internalType":"address","name":"implementation","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"stateMutability":"payable","type":"constructor"}],
        )
        """

    def testContractUploadRequest(self):
        """Test ContractUploadRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
