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

from fireblocks.models.token_link_not_multichain_compatible_http_error import (
    TokenLinkNotMultichainCompatibleHttpError,
)


class TestTokenLinkNotMultichainCompatibleHttpError(unittest.TestCase):
    """TokenLinkNotMultichainCompatibleHttpError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> TokenLinkNotMultichainCompatibleHttpError:
        """Test TokenLinkNotMultichainCompatibleHttpError
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TokenLinkNotMultichainCompatibleHttpError`
        """
        model = TokenLinkNotMultichainCompatibleHttpError()
        if include_optional:
            return TokenLinkNotMultichainCompatibleHttpError(
                message = 'Token link is not multichain compatible.',
                code = 400
            )
        else:
            return TokenLinkNotMultichainCompatibleHttpError(
                message = 'Token link is not multichain compatible.',
                code = 400,
        )
        """

    def testTokenLinkNotMultichainCompatibleHttpError(self):
        """Test TokenLinkNotMultichainCompatibleHttpError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
