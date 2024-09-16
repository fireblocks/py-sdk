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

from fireblocks.models.fetch_abi_request_dto import FetchAbiRequestDto


class TestFetchAbiRequestDto(unittest.TestCase):
    """FetchAbiRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FetchAbiRequestDto:
        """Test FetchAbiRequestDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FetchAbiRequestDto`
        """
        model = FetchAbiRequestDto()
        if include_optional:
            return FetchAbiRequestDto(
                base_asset_id = 'ETH',
                contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66'
            )
        else:
            return FetchAbiRequestDto(
                base_asset_id = 'ETH',
                contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66',
        )
        """

    def testFetchAbiRequestDto(self):
        """Test FetchAbiRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
