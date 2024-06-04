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

from fireblocks.models.asset_conflict_error_response import AssetConflictErrorResponse


class TestAssetConflictErrorResponse(unittest.TestCase):
    """AssetConflictErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetConflictErrorResponse:
        """Test AssetConflictErrorResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AssetConflictErrorResponse`
        """
        model = AssetConflictErrorResponse()
        if include_optional:
            return AssetConflictErrorResponse(
                message = 'Asset already listed',
                code = '3002'
            )
        else:
            return AssetConflictErrorResponse(
                message = 'Asset already listed',
                code = '3002',
        )
        """

    def testAssetConflictErrorResponse(self):
        """Test AssetConflictErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()