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

from fireblocks_client.models.delegation_summary_dto import DelegationSummaryDto


class TestDelegationSummaryDto(unittest.TestCase):
    """DelegationSummaryDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DelegationSummaryDto:
        """Test DelegationSummaryDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DelegationSummaryDto`
        """
        model = DelegationSummaryDto()
        if include_optional:
            return DelegationSummaryDto(
                active = [
                    fireblocks_client.models.amount_and_chain_descriptor.AmountAndChainDescriptor(
                        chain_descriptor = 'ETH', 
                        amount = '32.007149606', )
                    ],
                inactive = [
                    fireblocks_client.models.amount_and_chain_descriptor.AmountAndChainDescriptor(
                        chain_descriptor = 'ETH', 
                        amount = '32.007149606', )
                    ],
                rewards_amount = [
                    fireblocks_client.models.amount_and_chain_descriptor.AmountAndChainDescriptor(
                        chain_descriptor = 'ETH', 
                        amount = '32.007149606', )
                    ],
                total_staked = [
                    fireblocks_client.models.amount_and_chain_descriptor.AmountAndChainDescriptor(
                        chain_descriptor = 'ETH', 
                        amount = '32.007149606', )
                    ]
            )
        else:
            return DelegationSummaryDto(
                active = [
                    fireblocks_client.models.amount_and_chain_descriptor.AmountAndChainDescriptor(
                        chain_descriptor = 'ETH', 
                        amount = '32.007149606', )
                    ],
                inactive = [
                    fireblocks_client.models.amount_and_chain_descriptor.AmountAndChainDescriptor(
                        chain_descriptor = 'ETH', 
                        amount = '32.007149606', )
                    ],
                rewards_amount = [
                    fireblocks_client.models.amount_and_chain_descriptor.AmountAndChainDescriptor(
                        chain_descriptor = 'ETH', 
                        amount = '32.007149606', )
                    ],
                total_staked = [
                    fireblocks_client.models.amount_and_chain_descriptor.AmountAndChainDescriptor(
                        chain_descriptor = 'ETH', 
                        amount = '32.007149606', )
                    ],
        )
        """

    def testDelegationSummaryDto(self):
        """Test DelegationSummaryDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
