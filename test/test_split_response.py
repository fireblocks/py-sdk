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

from fireblocks.models.split_response import SplitResponse


class TestSplitResponse(unittest.TestCase):
    """SplitResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SplitResponse:
        """Test SplitResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SplitResponse`
        """
        model = SplitResponse()
        if include_optional:
            return SplitResponse(
                id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d'
            )
        else:
            return SplitResponse(
                id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d',
        )
        """

    def testSplitResponse(self):
        """Test SplitResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
