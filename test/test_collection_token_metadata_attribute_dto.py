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

from fireblocks.models.collection_token_metadata_attribute_dto import (
    CollectionTokenMetadataAttributeDto,
)


class TestCollectionTokenMetadataAttributeDto(unittest.TestCase):
    """CollectionTokenMetadataAttributeDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionTokenMetadataAttributeDto:
        """Test CollectionTokenMetadataAttributeDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CollectionTokenMetadataAttributeDto`
        """
        model = CollectionTokenMetadataAttributeDto()
        if include_optional:
            return CollectionTokenMetadataAttributeDto(
                trait_type = 'project_start',
                value = '30102000',
                display_type = 'date'
            )
        else:
            return CollectionTokenMetadataAttributeDto(
                trait_type = 'project_start',
                value = '30102000',
        )
        """

    def testCollectionTokenMetadataAttributeDto(self):
        """Test CollectionTokenMetadataAttributeDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()