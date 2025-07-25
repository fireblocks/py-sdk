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

from fireblocks.models.vault_accounts_tag_attachments_request import (
    VaultAccountsTagAttachmentsRequest,
)


class TestVaultAccountsTagAttachmentsRequest(unittest.TestCase):
    """VaultAccountsTagAttachmentsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VaultAccountsTagAttachmentsRequest:
        """Test VaultAccountsTagAttachmentsRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `VaultAccountsTagAttachmentsRequest`
        """
        model = VaultAccountsTagAttachmentsRequest()
        if include_optional:
            return VaultAccountsTagAttachmentsRequest(
                tag_ids = ["df4c0987-30da-4976-8dcf-bc2dd41ae331","a1b2c3d4-e5f6-7890-abcd-ef1234567890"],
                vault_account_ids = ["0","1"]
            )
        else:
            return VaultAccountsTagAttachmentsRequest(
                tag_ids = ["df4c0987-30da-4976-8dcf-bc2dd41ae331","a1b2c3d4-e5f6-7890-abcd-ef1234567890"],
                vault_account_ids = ["0","1"],
        )
        """

    def testVaultAccountsTagAttachmentsRequest(self):
        """Test VaultAccountsTagAttachmentsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
