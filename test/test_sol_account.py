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

from fireblocks.models.sol_account import SOLAccount


class TestSOLAccount(unittest.TestCase):
    """SOLAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SOLAccount:
        """Test SOLAccount
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SOLAccount`
        """
        model = SOLAccount()
        if include_optional:
            return SOLAccount(
                name = 'mint',
                signer = False,
                writable = True,
                address = '4PVcDXAkAgQkVx4puiSXdZ5H8BrTqUzstJBKKWFy3XsH'
            )
        else:
            return SOLAccount(
                name = 'mint',
        )
        """

    def testSOLAccount(self):
        """Test SOLAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
