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

from fireblocks.models.update_callback_handler_request import (
    UpdateCallbackHandlerRequest,
)


class TestUpdateCallbackHandlerRequest(unittest.TestCase):
    """UpdateCallbackHandlerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateCallbackHandlerRequest:
        """Test UpdateCallbackHandlerRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UpdateCallbackHandlerRequest`
        """
        model = UpdateCallbackHandlerRequest()
        if include_optional:
            return UpdateCallbackHandlerRequest(
                callback_handler = fireblocks.models.callback_handler_request.CallbackHandlerRequest(
                    url = 'https://example.com/callback-handler', 
                    public_key = '-----BEGIN PUBLIC KEY-----
... truncated ...-----END PUBLIC KEY-----', 
                    cert = '-----BEGIN CERTIFICATE-----
... truncated ...
-----END CERTIFICATE-----', )
            )
        else:
            return UpdateCallbackHandlerRequest(
        )
        """

    def testUpdateCallbackHandlerRequest(self):
        """Test UpdateCallbackHandlerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
