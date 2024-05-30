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

from fireblocks_client.models.list_owned_tokens_response import ListOwnedTokensResponse


class TestListOwnedTokensResponse(unittest.TestCase):
    """ListOwnedTokensResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListOwnedTokensResponse:
        """Test ListOwnedTokensResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ListOwnedTokensResponse`
        """
        model = ListOwnedTokensResponse()
        if include_optional:
            return ListOwnedTokensResponse(
                paging = fireblocks_client.models.paging.Paging(
                    next = '', ),
                data = [
                    fireblocks_client.models.token_response.TokenResponse(
                        id = '', 
                        token_id = '', 
                        standard = '', 
                        metadata_uri = '', 
                        cached_metadata_uri = '', 
                        media = [
                            fireblocks_client.models.media_entity_response.MediaEntityResponse(
                                url = '', 
                                content_type = 'IMAGE', )
                            ], 
                        spam = null, 
                        collection = null, 
                        blockchain_descriptor = 'ETH', 
                        description = '', 
                        name = '', )
                    ]
            )
        else:
            return ListOwnedTokensResponse(
        )
        """

    def testListOwnedTokensResponse(self):
        """Test ListOwnedTokensResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
