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

from fireblocks.models.audit_log_data import AuditLogData


class TestAuditLogData(unittest.TestCase):
    """AuditLogData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuditLogData:
        """Test AuditLogData
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AuditLogData`
        """
        model = AuditLogData()
        if include_optional:
            return AuditLogData(
                id = '',
                timestamp = '',
                created_at = '',
                user = '',
                subject = '',
                event = '',
                tenant_id = '',
                user_id = ''
            )
        else:
            return AuditLogData(
        )
        """

    def testAuditLogData(self):
        """Test AuditLogData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()