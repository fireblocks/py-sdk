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

from fireblocks.models.resend_notifications_by_resource_id_request import (
    ResendNotificationsByResourceIdRequest,
)


class TestResendNotificationsByResourceIdRequest(unittest.TestCase):
    """ResendNotificationsByResourceIdRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResendNotificationsByResourceIdRequest:
        """Test ResendNotificationsByResourceIdRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ResendNotificationsByResourceIdRequest`
        """
        model = ResendNotificationsByResourceIdRequest()
        if include_optional:
            return ResendNotificationsByResourceIdRequest(
                resource_id = '44fcead0-7053-4831-a53a-df7fb90d440f',
                exclude_statuses = ["IN_PROGRESS","FAILED"]
            )
        else:
            return ResendNotificationsByResourceIdRequest(
                resource_id = '44fcead0-7053-4831-a53a-df7fb90d440f',
        )
        """

    def testResendNotificationsByResourceIdRequest(self):
        """Test ResendNotificationsByResourceIdRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
