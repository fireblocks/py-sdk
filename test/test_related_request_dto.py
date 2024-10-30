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

from fireblocks.models.related_request_dto import RelatedRequestDto


class TestRelatedRequestDto(unittest.TestCase):
    """RelatedRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelatedRequestDto:
        """Test RelatedRequestDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RelatedRequestDto`
        """
        model = RelatedRequestDto()
        if include_optional:
            return RelatedRequestDto(
                status = 'deactivating',
                in_progress = False,
                amount = '0.05',
                tx_id = 'c80601f4-d7b1-4795-a8ee-b09cdb5b450c'
            )
        else:
            return RelatedRequestDto(
                status = 'deactivating',
                in_progress = False,
                amount = '0.05',
        )
        """

    def testRelatedRequestDto(self):
        """Test RelatedRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()