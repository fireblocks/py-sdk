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

from fireblocks.api.vaults_api import VaultsApi


class TestVaultsApi(unittest.TestCase):
    """VaultsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VaultsApi()

    def tearDown(self) -> None:
        pass

    def test_activate_asset_for_vault_account(self) -> None:
        """Test case for activate_asset_for_vault_account

        Activate a wallet in a vault account
        """
        pass

    def test_attach_tags_to_vault_accounts(self) -> None:
        """Test case for attach_tags_to_vault_accounts

        Attach tags to a vault accounts
        """
        pass

    def test_create_legacy_address(self) -> None:
        """Test case for create_legacy_address

        Convert a segwit address to legacy format
        """
        pass

    def test_create_multiple_accounts(self) -> None:
        """Test case for create_multiple_accounts

        Bulk creation of new vault accounts
        """
        pass

    def test_create_multiple_deposit_addresses(self) -> None:
        """Test case for create_multiple_deposit_addresses

        Bulk creation of new deposit addresses
        """
        pass

    def test_create_vault_account(self) -> None:
        """Test case for create_vault_account

        Create a new vault account
        """
        pass

    def test_create_vault_account_asset(self) -> None:
        """Test case for create_vault_account_asset

        Create a new wallet
        """
        pass

    def test_create_vault_account_asset_address(self) -> None:
        """Test case for create_vault_account_asset_address

        Create new asset deposit address
        """
        pass

    def test_detach_tags_from_vault_accounts(self) -> None:
        """Test case for detach_tags_from_vault_accounts

        Detach tags from a vault accounts
        """
        pass

    def test_get_asset_wallets(self) -> None:
        """Test case for get_asset_wallets

        List asset wallets (Paginated)
        """
        pass

    def test_get_create_multiple_deposit_addresses_job_status(self) -> None:
        """Test case for get_create_multiple_deposit_addresses_job_status

        Get job status of bulk creation of new deposit addresses
        """
        pass

    def test_get_create_multiple_vault_accounts_job_status(self) -> None:
        """Test case for get_create_multiple_vault_accounts_job_status

        Get job status of bulk creation of new vault accounts
        """
        pass

    def test_get_max_spendable_amount(self) -> None:
        """Test case for get_max_spendable_amount

        Get the maximum spendable amount in a single transaction.
        """
        pass

    def test_get_paged_vault_accounts(self) -> None:
        """Test case for get_paged_vault_accounts

        List vault accounts (Paginated)
        """
        pass

    def test_get_public_key_info(self) -> None:
        """Test case for get_public_key_info

        Get the public key information
        """
        pass

    def test_get_public_key_info_for_address(self) -> None:
        """Test case for get_public_key_info_for_address

        Get the public key for a vault account
        """
        pass

    def test_get_unspent_inputs(self) -> None:
        """Test case for get_unspent_inputs

        Get UTXO unspent inputs information
        """
        pass

    def test_get_vault_account(self) -> None:
        """Test case for get_vault_account

        Find a vault account by ID
        """
        pass

    def test_get_vault_account_asset(self) -> None:
        """Test case for get_vault_account_asset

        Get the asset balance for a vault account
        """
        pass

    def test_get_vault_account_asset_addresses_paginated(self) -> None:
        """Test case for get_vault_account_asset_addresses_paginated

        List addresses (Paginated)
        """
        pass

    def test_get_vault_assets(self) -> None:
        """Test case for get_vault_assets

        Get asset balance for chosen assets
        """
        pass

    def test_get_vault_balance_by_asset(self) -> None:
        """Test case for get_vault_balance_by_asset

        Get vault balance by asset
        """
        pass

    def test_hide_vault_account(self) -> None:
        """Test case for hide_vault_account

        Hide a vault account in the console
        """
        pass

    def test_set_customer_ref_id_for_address(self) -> None:
        """Test case for set_customer_ref_id_for_address

        Assign AML customer reference ID
        """
        pass

    def test_set_vault_account_auto_fuel(self) -> None:
        """Test case for set_vault_account_auto_fuel

        Turn autofueling on or off
        """
        pass

    def test_set_vault_account_customer_ref_id(self) -> None:
        """Test case for set_vault_account_customer_ref_id

        Set an AML/KYT customer reference ID for a vault account
        """
        pass

    def test_unhide_vault_account(self) -> None:
        """Test case for unhide_vault_account

        Unhide a vault account in the console
        """
        pass

    def test_update_vault_account(self) -> None:
        """Test case for update_vault_account

        Rename a vault account
        """
        pass

    def test_update_vault_account_asset_address(self) -> None:
        """Test case for update_vault_account_asset_address

        Update address description
        """
        pass

    def test_update_vault_account_asset_balance(self) -> None:
        """Test case for update_vault_account_asset_balance

        Refresh asset balance data
        """
        pass


if __name__ == "__main__":
    unittest.main()
