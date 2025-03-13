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

from fireblocks.models.destination_transfer_peer_path import DestinationTransferPeerPath


class TestDestinationTransferPeerPath(unittest.TestCase):
    """DestinationTransferPeerPath unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DestinationTransferPeerPath:
        """Test DestinationTransferPeerPath
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DestinationTransferPeerPath`
        """
        model = DestinationTransferPeerPath()
        if include_optional:
            return DestinationTransferPeerPath(
                type = 'VAULT_ACCOUNT',
                sub_type = 'BINANCE',
                id = '',
                name = '',
                wallet_id = '',
                one_time_address = fireblocks.models.one_time_address.OneTimeAddress(
                    address = '', 
                    tag = '', )
            )
        else:
            return DestinationTransferPeerPath(
                type = 'VAULT_ACCOUNT',
        )
        """

    def testDestinationTransferPeerPath(self):
        """Test DestinationTransferPeerPath"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
