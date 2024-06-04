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

from fireblocks.api.web3_connections_api import Web3ConnectionsApi


class TestWeb3ConnectionsApi(unittest.TestCase):
    """Web3ConnectionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = Web3ConnectionsApi()

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create a new Web3 connection.
        """
        pass

    def test_get(self) -> None:
        """Test case for get

        List all open Web3 connections.
        """
        pass

    def test_remove(self) -> None:
        """Test case for remove

        Remove an existing Web3 connection.
        """
        pass

    def test_submit(self) -> None:
        """Test case for submit

        Respond to a pending Web3 connection request.
        """
        pass


if __name__ == "__main__":
    unittest.main()