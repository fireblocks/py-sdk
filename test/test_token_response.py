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

from fireblocks.models.token_response import TokenResponse


class TestTokenResponse(unittest.TestCase):
    """TokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenResponse:
        """Test TokenResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TokenResponse`
        """
        model = TokenResponse()
        if include_optional:
            return TokenResponse(
                id = '',
                token_id = '',
                standard = '',
                metadata_uri = '',
                cached_metadata_uri = '',
                media = [
                    fireblocks.models.media_entity_response.MediaEntityResponse(
                        url = '', 
                        content_type = 'IMAGE', )
                    ],
                spam = fireblocks.models.spam_token_response.SpamTokenResponse(
                    result = True, ),
                collection = fireblocks.models.token_collection_response.TokenCollectionResponse(
                    id = '', 
                    name = '', 
                    symbol = '', ),
                blockchain_descriptor = 'ETH',
                description = '',
                name = ''
            )
        else:
            return TokenResponse(
                id = '',
                token_id = '',
                standard = '',
                blockchain_descriptor = 'ETH',
        )
        """

    def testTokenResponse(self):
        """Test TokenResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
