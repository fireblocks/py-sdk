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

from fireblocks_client.models.smart_transfer_user_groups_response import (
    SmartTransferUserGroupsResponse,
)


class TestSmartTransferUserGroupsResponse(unittest.TestCase):
    """SmartTransferUserGroupsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmartTransferUserGroupsResponse:
        """Test SmartTransferUserGroupsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SmartTransferUserGroupsResponse`
        """
        model = SmartTransferUserGroupsResponse()
        if include_optional:
            return SmartTransferUserGroupsResponse(
                message = 'Success',
                data = fireblocks_client.models.smart_transfer_user_groups.SmartTransferUserGroups(
                    user_group_ids = [
                        ''
                        ], )
            )
        else:
            return SmartTransferUserGroupsResponse(
                message = 'Success',
        )
        """

    def testSmartTransferUserGroupsResponse(self):
        """Test SmartTransferUserGroupsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
