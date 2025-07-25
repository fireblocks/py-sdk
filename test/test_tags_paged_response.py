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

from fireblocks.models.tags_paged_response import TagsPagedResponse


class TestTagsPagedResponse(unittest.TestCase):
    """TagsPagedResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagsPagedResponse:
        """Test TagsPagedResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TagsPagedResponse`
        """
        model = TagsPagedResponse()
        if include_optional:
            return TagsPagedResponse(
                data = [
                    fireblocks.models.tag.Tag(
                        id = 'df4c0987-30da-4976-8dcf-bc2dd41ae331', 
                        label = 'VIP', 
                        description = 'Tag for VIP customers', )
                    ],
                next = 'MjAyNS0wNy0wOSAxMDo1MzoxMy40NTI=:NA=='
            )
        else:
            return TagsPagedResponse(
                data = [
                    fireblocks.models.tag.Tag(
                        id = 'df4c0987-30da-4976-8dcf-bc2dd41ae331', 
                        label = 'VIP', 
                        description = 'Tag for VIP customers', )
                    ],
                next = 'MjAyNS0wNy0wOSAxMDo1MzoxMy40NTI=:NA==',
        )
        """

    def testTagsPagedResponse(self):
        """Test TagsPagedResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
