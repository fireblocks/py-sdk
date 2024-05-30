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

from fireblocks.api.nfts_api import NFTsApi


class TestNFTsApi(unittest.TestCase):
    """NFTsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NFTsApi()

    def tearDown(self) -> None:
        pass

    def test_get_nft(self) -> None:
        """Test case for get_nft

        List token data by ID
        """
        pass

    def test_get_nfts(self) -> None:
        """Test case for get_nfts

        List tokens by IDs
        """
        pass

    def test_get_ownership_tokens(self) -> None:
        """Test case for get_ownership_tokens

        List all owned tokens (paginated)
        """
        pass

    def test_list_owned_collections(self) -> None:
        """Test case for list_owned_collections

        List owned collections (paginated)
        """
        pass

    def test_list_owned_tokens(self) -> None:
        """Test case for list_owned_tokens

        List all distinct owned tokens (paginated)
        """
        pass

    def test_refresh_nft_metadata(self) -> None:
        """Test case for refresh_nft_metadata

        Refresh token metadata
        """
        pass

    def test_update_ownership_tokens(self) -> None:
        """Test case for update_ownership_tokens

        Refresh vault account tokens
        """
        pass

    def test_update_token_ownership_status(self) -> None:
        """Test case for update_token_ownership_status

        Update token ownership status
        """
        pass

    def test_update_tokens_ownership_spam(self) -> None:
        """Test case for update_tokens_ownership_spam

        Update tokens ownership spam property
        """
        pass

    def test_update_tokens_ownership_status(self) -> None:
        """Test case for update_tokens_ownership_status

        Update tokens ownership status
        """
        pass


if __name__ == "__main__":
    unittest.main()
