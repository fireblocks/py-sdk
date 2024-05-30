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

from fireblocks_client.models.network_id_routing_policy_value import (
    NetworkIdRoutingPolicyValue,
)


class TestNetworkIdRoutingPolicyValue(unittest.TestCase):
    """NetworkIdRoutingPolicyValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkIdRoutingPolicyValue:
        """Test NetworkIdRoutingPolicyValue
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `NetworkIdRoutingPolicyValue`
        """
        model = NetworkIdRoutingPolicyValue()
        if include_optional:
            return NetworkIdRoutingPolicyValue(
                scheme = 'NONE',
                dst_type = 'FIAT_ACCOUNT',
                dst_id = ''
            )
        else:
            return NetworkIdRoutingPolicyValue(
                scheme = 'NONE',
                dst_type = 'FIAT_ACCOUNT',
                dst_id = '',
        )
        """

    def testNetworkIdRoutingPolicyValue(self):
        """Test NetworkIdRoutingPolicyValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
