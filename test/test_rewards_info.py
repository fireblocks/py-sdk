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

from fireblocks_client.models.rewards_info import RewardsInfo


class TestRewardsInfo(unittest.TestCase):
    """RewardsInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RewardsInfo:
        """Test RewardsInfo
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RewardsInfo`
        """
        model = RewardsInfo()
        if include_optional:
            return RewardsInfo(
                pending_rewards = ''
            )
        else:
            return RewardsInfo(
        )
        """

    def testRewardsInfo(self):
        """Test RewardsInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
