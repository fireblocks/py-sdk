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

from fireblocks.models.asset_not_found_error_response import AssetNotFoundErrorResponse


class TestAssetNotFoundErrorResponse(unittest.TestCase):
    """AssetNotFoundErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetNotFoundErrorResponse:
        """Test AssetNotFoundErrorResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AssetNotFoundErrorResponse`
        """
        model = AssetNotFoundErrorResponse()
        if include_optional:
            return AssetNotFoundErrorResponse(
                message = 'Asset with specified ID not found',
                code = 1504
            )
        else:
            return AssetNotFoundErrorResponse(
                message = 'Asset with specified ID not found',
                code = 1504,
        )
        """

    def testAssetNotFoundErrorResponse(self):
        """Test AssetNotFoundErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
