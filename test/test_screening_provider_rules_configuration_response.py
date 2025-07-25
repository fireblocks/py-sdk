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

from fireblocks.models.screening_provider_rules_configuration_response import (
    ScreeningProviderRulesConfigurationResponse,
)


class TestScreeningProviderRulesConfigurationResponse(unittest.TestCase):
    """ScreeningProviderRulesConfigurationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> ScreeningProviderRulesConfigurationResponse:
        """Test ScreeningProviderRulesConfigurationResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ScreeningProviderRulesConfigurationResponse`
        """
        model = ScreeningProviderRulesConfigurationResponse()
        if include_optional:
            return ScreeningProviderRulesConfigurationResponse(
                direction = 'INBOUND',
                status = 'COMPLETED',
                amount_usd = 1.337,
                amount = 1.337,
                asset = '',
                action = 'ACCEPT'
            )
        else:
            return ScreeningProviderRulesConfigurationResponse(
                action = 'ACCEPT',
        )
        """

    def testScreeningProviderRulesConfigurationResponse(self):
        """Test ScreeningProviderRulesConfigurationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
