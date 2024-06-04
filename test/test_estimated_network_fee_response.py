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

from fireblocks.models.estimated_network_fee_response import EstimatedNetworkFeeResponse


class TestEstimatedNetworkFeeResponse(unittest.TestCase):
    """EstimatedNetworkFeeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimatedNetworkFeeResponse:
        """Test EstimatedNetworkFeeResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EstimatedNetworkFeeResponse`
        """
        model = EstimatedNetworkFeeResponse()
        if include_optional:
            return EstimatedNetworkFeeResponse(
                low = fireblocks.models.network_fee.NetworkFee(
                    fee_per_byte = '', 
                    gas_price = '', 
                    network_fee = '', 
                    base_fee = '', 
                    priority_fee = '', ),
                medium = fireblocks.models.network_fee.NetworkFee(
                    fee_per_byte = '', 
                    gas_price = '', 
                    network_fee = '', 
                    base_fee = '', 
                    priority_fee = '', ),
                high = fireblocks.models.network_fee.NetworkFee(
                    fee_per_byte = '', 
                    gas_price = '', 
                    network_fee = '', 
                    base_fee = '', 
                    priority_fee = '', )
            )
        else:
            return EstimatedNetworkFeeResponse(
                low = fireblocks.models.network_fee.NetworkFee(
                    fee_per_byte = '', 
                    gas_price = '', 
                    network_fee = '', 
                    base_fee = '', 
                    priority_fee = '', ),
                medium = fireblocks.models.network_fee.NetworkFee(
                    fee_per_byte = '', 
                    gas_price = '', 
                    network_fee = '', 
                    base_fee = '', 
                    priority_fee = '', ),
                high = fireblocks.models.network_fee.NetworkFee(
                    fee_per_byte = '', 
                    gas_price = '', 
                    network_fee = '', 
                    base_fee = '', 
                    priority_fee = '', ),
        )
        """

    def testEstimatedNetworkFeeResponse(self):
        """Test EstimatedNetworkFeeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()