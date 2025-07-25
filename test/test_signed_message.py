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

from fireblocks.models.signed_message import SignedMessage


class TestSignedMessage(unittest.TestCase):
    """SignedMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignedMessage:
        """Test SignedMessage
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SignedMessage`
        """
        model = SignedMessage()
        if include_optional:
            return SignedMessage(
                content = '',
                algorithm = 'MPC_ECDSA_SECP256K1',
                derivation_path = [
                    1.337
                    ],
                signature = fireblocks.models.signed_message_signature.SignedMessage_signature(
                    full_sig = '', 
                    r = '', 
                    s = '', 
                    v = 1.337, ),
                public_key = ''
            )
        else:
            return SignedMessage(
        )
        """

    def testSignedMessage(self):
        """Test SignedMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
