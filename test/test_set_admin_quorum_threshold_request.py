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

from fireblocks_client.models.set_admin_quorum_threshold_request import (
    SetAdminQuorumThresholdRequest,
)


class TestSetAdminQuorumThresholdRequest(unittest.TestCase):
    """SetAdminQuorumThresholdRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetAdminQuorumThresholdRequest:
        """Test SetAdminQuorumThresholdRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SetAdminQuorumThresholdRequest`
        """
        model = SetAdminQuorumThresholdRequest()
        if include_optional:
            return SetAdminQuorumThresholdRequest(
                admin_quorum_threshold = 1.337
            )
        else:
            return SetAdminQuorumThresholdRequest(
        )
        """

    def testSetAdminQuorumThresholdRequest(self):
        """Test SetAdminQuorumThresholdRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
