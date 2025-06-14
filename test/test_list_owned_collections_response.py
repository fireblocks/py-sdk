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

from fireblocks.models.list_owned_collections_response import (
    ListOwnedCollectionsResponse,
)


class TestListOwnedCollectionsResponse(unittest.TestCase):
    """ListOwnedCollectionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListOwnedCollectionsResponse:
        """Test ListOwnedCollectionsResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ListOwnedCollectionsResponse`
        """
        model = ListOwnedCollectionsResponse()
        if include_optional:
            return ListOwnedCollectionsResponse(
                paging = fireblocks.models.paging.Paging(
                    next = '', ),
                data = [
                    fireblocks.models.collection_ownership_response.CollectionOwnershipResponse(
                        id = '', 
                        name = '', 
                        symbol = '', 
                        standard = '', 
                        blockchain_descriptor = 'ETH', 
                        contract_address = '', )
                    ]
            )
        else:
            return ListOwnedCollectionsResponse(
        )
        """

    def testListOwnedCollectionsResponse(self):
        """Test ListOwnedCollectionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
