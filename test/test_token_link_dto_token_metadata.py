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

from fireblocks.models.token_link_dto_token_metadata import TokenLinkDtoTokenMetadata


class TestTokenLinkDtoTokenMetadata(unittest.TestCase):
    """TokenLinkDtoTokenMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenLinkDtoTokenMetadata:
        """Test TokenLinkDtoTokenMetadata
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TokenLinkDtoTokenMetadata`
        """
        model = TokenLinkDtoTokenMetadata()
        if include_optional:
            return TokenLinkDtoTokenMetadata(
                asset_id = 'BQ5R_MY_TOKEN',
                name = 'Rarible',
                symbol = 'RARI',
                network_protocol = 'ETH',
                total_supply = '1000000000000000',
                holders_count = 6,
                type = 'ERC20',
                contract_address = '0x1234567890abcdef1234567890abcdef12345678',
                issuer_address = 'rGyXjc5d7s17vvt3NtKKascvJrnSxV21kQ',
                testnet = True,
                blockchain = 'ETH_TEST5',
                decimals = 18,
                vault_account_id = '0',
                fb_collection_id = '911fe739f0d4d123c98fd366c3bed35c6e30c00e',
                standard = '["ERC721","ERC1155","FA2"]',
                blockchain_descriptor = 'ETH',
                id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb',
                blockchain_id = 'B7QG017M',
                contract_template_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d'
            )
        else:
            return TokenLinkDtoTokenMetadata(
                asset_id = 'BQ5R_MY_TOKEN',
                contract_address = '0x1234567890abcdef1234567890abcdef12345678',
                fb_collection_id = '911fe739f0d4d123c98fd366c3bed35c6e30c00e',
                blockchain_descriptor = 'ETH',
                id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb',
                blockchain_id = 'B7QG017M',
                contract_template_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d',
        )
        """

    def testTokenLinkDtoTokenMetadata(self):
        """Test TokenLinkDtoTokenMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
