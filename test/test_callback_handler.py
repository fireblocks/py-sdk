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

from fireblocks.models.callback_handler import CallbackHandler


class TestCallbackHandler(unittest.TestCase):
    """CallbackHandler unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CallbackHandler:
        """Test CallbackHandler
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CallbackHandler`
        """
        model = CallbackHandler()
        if include_optional:
            return CallbackHandler(
                url = 'https://example.com/callback-handler',
                public_key = '-----BEGIN PUBLIC KEY-----
... truncated ...
-----END PUBLIC KEY-----',
                cert_public_key_hash = ''
            )
        else:
            return CallbackHandler(
                url = 'https://example.com/callback-handler',
        )
        """

    def testCallbackHandler(self):
        """Test CallbackHandler"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
