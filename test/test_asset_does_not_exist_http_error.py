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

from fireblocks.models.asset_does_not_exist_http_error import AssetDoesNotExistHttpError


class TestAssetDoesNotExistHttpError(unittest.TestCase):
    """AssetDoesNotExistHttpError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetDoesNotExistHttpError:
        """Test AssetDoesNotExistHttpError
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AssetDoesNotExistHttpError`
        """
        model = AssetDoesNotExistHttpError()
        if include_optional:
            return AssetDoesNotExistHttpError(
                status_code = 404,
                message = '',
                error = 'Not Found'
            )
        else:
            return AssetDoesNotExistHttpError(
        )
        """

    def testAssetDoesNotExistHttpError(self):
        """Test AssetDoesNotExistHttpError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
