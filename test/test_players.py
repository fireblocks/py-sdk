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

from fireblocks.models.players import Players


class TestPlayers(unittest.TestCase):
    """Players unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Players:
        """Test Players
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Players`
        """
        model = Players()
        if include_optional:
            return Players(
                id = '47d3383e-37a3-43d5-90a4-de0ca8c5e258',
                type = 'MOBILE'
            )
        else:
            return Players(
                id = '47d3383e-37a3-43d5-90a4-de0ca8c5e258',
                type = 'MOBILE',
        )
        """

    def testPlayers(self):
        """Test Players"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
