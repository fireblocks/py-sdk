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

from fireblocks_client.models.create_token_request_dto import CreateTokenRequestDto


class TestCreateTokenRequestDto(unittest.TestCase):
    """CreateTokenRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTokenRequestDto:
        """Test CreateTokenRequestDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateTokenRequestDto`
        """
        model = CreateTokenRequestDto()
        if include_optional:
            return CreateTokenRequestDto(
                blockchain_id = 'B7QG017M',
                asset_id = 'ETH_TEST5',
                vault_account_id = '0',
                create_params = None,
                display_name = ''
            )
        else:
            return CreateTokenRequestDto(
                vault_account_id = '0',
                create_params = None,
        )
        """

    def testCreateTokenRequestDto(self):
        """Test CreateTokenRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
