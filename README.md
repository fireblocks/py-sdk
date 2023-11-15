[![PyPI version](https://badge.fury.io/py/fireblocks.svg)](https://badge.fury.io/py/fireblocks)

# Fireblocks SDK

The Fireblocks SDK allows developers to seamlessly integrate with the Fireblocks platform and perform a variety of operations, including managing vault accounts and executing transactions securely.

For detailed documentation and additional resources, please refer to the [Fireblocks Developer Portal](https://developers.fireblocks.com/).

> **Warning**
> This package is currently in a beta stage and should be used at your own risk.
> The provided interfaces might go through backwards-incompatibale changes.
> For a more stable SDK, please use the [Fireblocks Python SDK](https://github.com/fireblocks/fireblocks-sdk-py)

## Requirements.

Python &gt;&#x3D;3.7

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
If the python package is hosted on a repository, you can install directly using:
```sh
pip install fireblocks
```
Then import the package:
```python
import fireblocks_client
```

## Usage
<p><strong>Using Environment Variables</strong><br>
You can initialize the SDK using environment variables from your .env file or by setting them programmatically:</p>

```python
// Set the environment variables
os.environ["FIREBLOCKS_BASE_PATH"] = 'https://sandbox-api.fireblocks.io/v1'
os.environ["FIREBLOCKS_API_KEY"] = '<api-key>'
os.environ["FIREBLOCKS_SECRET_KEY"]  = open("./fireblocks_secret.key", "r").read()
```
<p><strong>Providing Local Variables</strong><br>
Alternatively, you can directly pass the required parameters when initializing the Fireblocks API instance:</p>

```python
FIREBLOCKS_API_SECRET_PATH = "./fireblocks_secret.key";

// Initialize a Fireblocks API instance with local variables
config = Configuration(api_key="my-api-key", base_path="https://sandbox-api.fireblocks.io/v1",secret_key=open(FIREBLOCKS_API_SECRET_PATH, "r").read())
vault_api = vaults_api.VaultsApi(config);
```

## Examples

<p><strong>Create a Vault Account</strong><br>
To create a new vault account, you can use the following function:</p>

```python
create_vault_account_response = vault_api.create_vault_account(body={"name": "New Vault"})
```

<p><strong>Create a Transaction</strong><br>
To make a transaction between vault accounts, you can use the following function:</p>

```python
tx_request = tx_api_instance.create_transaction(
        body=TransactionRequest(
            source=TransferPeerPath(id="0", type="VAULT_ACCOUNT"),
            destination=DestinationTransferPeerPath(
                id="0", type="VAULT_ACCOUNT"
            ),
            assetId="ETH_TEST3",
            amount="0.001",
        )
    )
```

## Documentation for API Endpoints

All URIs are relative to https://developers.fireblocks.com/reference/

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuditLogsApi* | [**get_audits**](docs/apis/tags/AuditLogsApi.md#get_audits) | **get** /audits | Get audit logs
*BlockchainsAssetsApi* | [**get_supported_assets**](docs/apis/tags/BlockchainsAssetsApi.md#get_supported_assets) | **get** /supported_assets | List all asset types supported by Fireblocks
*ContractsApi* | [**add_asset_to_contract**](docs/apis/tags/ContractsApi.md#add_asset_to_contract) | **post** /contracts/{contractId}/{assetId} | Add an asset to a contract
*ContractsApi* | [**create_contract**](docs/apis/tags/ContractsApi.md#create_contract) | **post** /contracts | Create a contract
*ContractsApi* | [**delete_contract**](docs/apis/tags/ContractsApi.md#delete_contract) | **delete** /contracts/{contractId} | Delete a contract
*ContractsApi* | [**get_asset_in_contract**](docs/apis/tags/ContractsApi.md#get_asset_in_contract) | **get** /contracts/{contractId}/{assetId} | Find a contract asset
*ContractsApi* | [**get_contract_by_id**](docs/apis/tags/ContractsApi.md#get_contract_by_id) | **get** /contracts/{contractId} | Find a specific contract
*ContractsApi* | [**get_contracts**](docs/apis/tags/ContractsApi.md#get_contracts) | **get** /contracts | List contracts
*ContractsApi* | [**remove_asset_from_contract**](docs/apis/tags/ContractsApi.md#remove_asset_from_contract) | **delete** /contracts/{contractId}/{assetId} | Delete a contract asset
*ExchangeAccountsApi* | [**convert_assets**](docs/apis/tags/ExchangeAccountsApi.md#convert_assets) | **post** /exchange_accounts/{exchangeAccountId}/convert | Convert exchange account funds from the source asset to the destination asset. Coinbase (USD to USDC, USDC to USD) and Bitso (MXN to USD) are supported conversions.
*ExchangeAccountsApi* | [**get_exchange_account_asset**](docs/apis/tags/ExchangeAccountsApi.md#get_exchange_account_asset) | **get** /exchange_accounts/{exchangeAccountId}/{assetId} | Find an asset for an exchange account
*ExchangeAccountsApi* | [**get_exchange_account_by_id**](docs/apis/tags/ExchangeAccountsApi.md#get_exchange_account_by_id) | **get** /exchange_accounts/{exchangeAccountId} | Find a specific exchange account
*ExchangeAccountsApi* | [**get_exchange_accounts**](docs/apis/tags/ExchangeAccountsApi.md#get_exchange_accounts) | **get** /exchange_accounts | List exchange accounts
*ExchangeAccountsApi* | [**internal_transfer**](docs/apis/tags/ExchangeAccountsApi.md#internal_transfer) | **post** /exchange_accounts/{exchangeAccountId}/internal_transfer | Internal tranfer for exchange accounts
*ExternalWalletsApi* | [**add_asset_to_external_wallet**](docs/apis/tags/ExternalWalletsApi.md#add_asset_to_external_wallet) | **post** /external_wallets/{walletId}/{assetId} | Add an asset to an external wallet.
*ExternalWalletsApi* | [**create_external_wallet**](docs/apis/tags/ExternalWalletsApi.md#create_external_wallet) | **post** /external_wallets | Create an external wallet
*ExternalWalletsApi* | [**delete_external_wallet**](docs/apis/tags/ExternalWalletsApi.md#delete_external_wallet) | **delete** /external_wallets/{walletId} | Delete an external wallet
*ExternalWalletsApi* | [**get_asset_in_external_wallet**](docs/apis/tags/ExternalWalletsApi.md#get_asset_in_external_wallet) | **get** /external_wallets/{walletId}/{assetId} | Get an asset from an external wallet
*ExternalWalletsApi* | [**get_external_wallet_by_id**](docs/apis/tags/ExternalWalletsApi.md#get_external_wallet_by_id) | **get** /external_wallets/{walletId} | Find an external wallet
*ExternalWalletsApi* | [**get_external_wallets**](docs/apis/tags/ExternalWalletsApi.md#get_external_wallets) | **get** /external_wallets | List external wallets
*ExternalWalletsApi* | [**remove_asset_from_external_wallet**](docs/apis/tags/ExternalWalletsApi.md#remove_asset_from_external_wallet) | **delete** /external_wallets/{walletId}/{assetId} | Delete an asset from an external wallet
*ExternalWalletsApi* | [**set_customer_ref_id_for_external_wallet**](docs/apis/tags/ExternalWalletsApi.md#set_customer_ref_id_for_external_wallet) | **post** /external_wallets/{walletId}/set_customer_ref_id | Set an AML customer reference ID for an external wallet
*FiatAccountsApi* | [**deposit_funds_from_linked_dda**](docs/apis/tags/FiatAccountsApi.md#deposit_funds_from_linked_dda) | **post** /fiat_accounts/{accountId}/deposit_from_linked_dda | Deposit funds from DDA
*FiatAccountsApi* | [**get_fiat_account_by_id**](docs/apis/tags/FiatAccountsApi.md#get_fiat_account_by_id) | **get** /fiat_accounts/{accountId} | Find a specific fiat account
*FiatAccountsApi* | [**get_fiat_accounts**](docs/apis/tags/FiatAccountsApi.md#get_fiat_accounts) | **get** /fiat_accounts | List fiat accounts
*FiatAccountsApi* | [**redeem_funds_to_linked_dda**](docs/apis/tags/FiatAccountsApi.md#redeem_funds_to_linked_dda) | **post** /fiat_accounts/{accountId}/redeem_to_linked_dda | Redeem funds to DDA
*GasStationsApi* | [**get_gas_station**](docs/apis/tags/GasStationsApi.md#get_gas_station) | **get** /gas_station | Get gas station settings
*GasStationsApi* | [**get_gas_station_by_asset_id**](docs/apis/tags/GasStationsApi.md#get_gas_station_by_asset_id) | **get** /gas_station/{assetId} | Get gas station settings by asset
*GasStationsApi* | [**update_gas_station_configuration**](docs/apis/tags/GasStationsApi.md#update_gas_station_configuration) | **put** /gas_station/configuration | Edit gas station settings
*GasStationsApi* | [**update_gas_station_configuration_by_asset_id**](docs/apis/tags/GasStationsApi.md#update_gas_station_configuration_by_asset_id) | **put** /gas_station/configuration/{assetId} | Edit gas station settings for an asset
*InternalWalletsApi* | [**create_internal_wallet**](docs/apis/tags/InternalWalletsApi.md#create_internal_wallet) | **post** /internal_wallets | Create an internal wallet
*InternalWalletsApi* | [**create_internal_wallet_asset**](docs/apis/tags/InternalWalletsApi.md#create_internal_wallet_asset) | **post** /internal_wallets/{walletId}/{assetId} | Add an asset to an internal wallet
*InternalWalletsApi* | [**delete_internal_wallet**](docs/apis/tags/InternalWalletsApi.md#delete_internal_wallet) | **delete** /internal_wallets/{walletId} | Delete an internal wallet
*InternalWalletsApi* | [**delete_internal_wallet_asset**](docs/apis/tags/InternalWalletsApi.md#delete_internal_wallet_asset) | **delete** /internal_wallets/{walletId}/{assetId} | Delete a whitelisted address from an internal wallet
*InternalWalletsApi* | [**get_internal_wallet_asset**](docs/apis/tags/InternalWalletsApi.md#get_internal_wallet_asset) | **get** /internal_wallets/{walletId}/{assetId} | Get an asset from an internal wallet
*InternalWalletsApi* | [**get_internal_wallet_by_id**](docs/apis/tags/InternalWalletsApi.md#get_internal_wallet_by_id) | **get** /internal_wallets/{walletId} | Get assets for internal wallet
*InternalWalletsApi* | [**get_internal_wallets**](docs/apis/tags/InternalWalletsApi.md#get_internal_wallets) | **get** /internal_wallets | List internal wallets
*InternalWalletsApi* | [**set_customer_ref_id_for_internal_wallet**](docs/apis/tags/InternalWalletsApi.md#set_customer_ref_id_for_internal_wallet) | **post** /internal_wallets/{walletId}/set_customer_ref_id | Set an AML/KYT customer reference ID for an internal wallet
*NFTsApi* | [**get_nft**](docs/apis/tags/NFTsApi.md#get_nft) | **get** /nfts/tokens/{id} | List token data by ID
*NFTsApi* | [**get_nfts**](docs/apis/tags/NFTsApi.md#get_nfts) | **get** /nfts/tokens | List tokens by IDs
*NFTsApi* | [**get_ownership_tokens**](docs/apis/tags/NFTsApi.md#get_ownership_tokens) | **get** /nfts/ownership/tokens | List all owned tokens (paginated)
*NFTsApi* | [**list_owned_collections**](docs/apis/tags/NFTsApi.md#list_owned_collections) | **get** /nfts/ownership/collections | List owned collections (paginated)
*NFTsApi* | [**refresh_nft_metadata**](docs/apis/tags/NFTsApi.md#refresh_nft_metadata) | **put** /nfts/tokens/{id} | Refresh token metadata
*NFTsApi* | [**update_ownership_tokens**](docs/apis/tags/NFTsApi.md#update_ownership_tokens) | **put** /nfts/ownership/tokens | Refresh vault account tokens
*NFTsApi* | [**update_token_ownership_status**](docs/apis/tags/NFTsApi.md#update_token_ownership_status) | **put** /nfts/ownership/tokens/{id}/status | Update token ownership status
*NetworkConnectionsApi* | [**check_third_party_routing_for_network_connection**](docs/apis/tags/NetworkConnectionsApi.md#check_third_party_routing_for_network_connection) | **get** /network_connections/{connectionId}/is_third_party_routing/{assetType} | Retrieve third-party network routing validation by asset type.
*NetworkConnectionsApi* | [**create_network_connection**](docs/apis/tags/NetworkConnectionsApi.md#create_network_connection) | **post** /network_connections | Creates a new network connection
*NetworkConnectionsApi* | [**create_network_id**](docs/apis/tags/NetworkConnectionsApi.md#create_network_id) | **post** /network_ids | Creates a new Network ID
*NetworkConnectionsApi* | [**delete_network_connection**](docs/apis/tags/NetworkConnectionsApi.md#delete_network_connection) | **delete** /network_connections/{connectionId} | Deletes a network connection by ID
*NetworkConnectionsApi* | [**delete_network_id**](docs/apis/tags/NetworkConnectionsApi.md#delete_network_id) | **delete** /network_ids/{networkId} | Deletes specific network ID.
*NetworkConnectionsApi* | [**get_network_connection_by_id**](docs/apis/tags/NetworkConnectionsApi.md#get_network_connection_by_id) | **get** /network_connections/{connectionId} | Get a network connection
*NetworkConnectionsApi* | [**get_network_connections**](docs/apis/tags/NetworkConnectionsApi.md#get_network_connections) | **get** /network_connections | List network connections
*NetworkConnectionsApi* | [**get_network_id_by_id**](docs/apis/tags/NetworkConnectionsApi.md#get_network_id_by_id) | **get** /network_ids/{networkId} | Returns specific network ID.
*NetworkConnectionsApi* | [**get_network_ids**](docs/apis/tags/NetworkConnectionsApi.md#get_network_ids) | **get** /network_ids | Returns all network IDs, both local IDs and discoverable remote IDs
*NetworkConnectionsApi* | [**set_discoverability_for_network_id**](docs/apis/tags/NetworkConnectionsApi.md#set_discoverability_for_network_id) | **patch** /network_ids/{networkId}/set_discoverability | Update network ID&#x27;s discoverability.
*NetworkConnectionsApi* | [**set_network_id_name**](docs/apis/tags/NetworkConnectionsApi.md#set_network_id_name) | **patch** /network_ids/{networkId}/set_name | Update network ID&#x27;s name.
*NetworkConnectionsApi* | [**set_routing_policy_for_network_connection**](docs/apis/tags/NetworkConnectionsApi.md#set_routing_policy_for_network_connection) | **patch** /network_connections/{connectionId}/set_routing_policy | Update network connection routing policy.
*NetworkConnectionsApi* | [**set_routing_policy_for_network_id**](docs/apis/tags/NetworkConnectionsApi.md#set_routing_policy_for_network_id) | **patch** /network_ids/{networkId}/set_routing_policy | Update network id routing policy.
*OTABetaApi* | [**get_ota_status**](docs/apis/tags/OTABetaApi.md#get_ota_status) | **get** /management/ota | Returns current OTA status
*OTABetaApi* | [**set_ota_status**](docs/apis/tags/OTABetaApi.md#set_ota_status) | **post** /management/ota | Enable or disable transactions to OTA
*OffExchangesApi* | [**add_off_exchange**](docs/apis/tags/OffExchangesApi.md#add_off_exchange) | **post** /off_exchange/add | add collateral
*OffExchangesApi* | [**get_off_exchange_collateral_accounts**](docs/apis/tags/OffExchangesApi.md#get_off_exchange_collateral_accounts) | **get** /off_exchange/collateral_accounts/{mainExchangeAccountId} | Find a specific collateral exchange account
*OffExchangesApi* | [**get_off_exchange_settlement_transactions**](docs/apis/tags/OffExchangesApi.md#get_off_exchange_settlement_transactions) | **get** /off_exchange/settlements/transactions | get settlements transactions from exchange
*OffExchangesApi* | [**remove_off_exchange**](docs/apis/tags/OffExchangesApi.md#remove_off_exchange) | **post** /off_exchange/remove | remove collateral
*OffExchangesApi* | [**settle_off_exchange_trades**](docs/apis/tags/OffExchangesApi.md#settle_off_exchange_trades) | **post** /off_exchange/settlements/trader | create settlement for a trader
*PaymentsPayoutApi* | [**create_payout**](docs/apis/tags/PaymentsPayoutApi.md#create_payout) | **post** /payments/payout | Create a payout instruction set
*PaymentsPayoutApi* | [**execute_payout_action**](docs/apis/tags/PaymentsPayoutApi.md#execute_payout_action) | **post** /payments/payout/{payoutId}/actions/execute | Execute a payout instruction set
*PaymentsPayoutApi* | [**get_payout_by_id**](docs/apis/tags/PaymentsPayoutApi.md#get_payout_by_id) | **get** /payments/payout/{payoutId} | Get the status of a payout instruction set
*PaymentsCrossBorderSettlementApi* | [**create_xb_settlement_config**](docs/apis/tags/PaymentsCrossBorderSettlementApi.md#create_xb_settlement_config) | **post** /payments/xb-settlements/configs | Create a new cross-border settlement configuration
*PaymentsCrossBorderSettlementApi* | [**create_xb_settlement_flow**](docs/apis/tags/PaymentsCrossBorderSettlementApi.md#create_xb_settlement_flow) | **post** /payments/xb-settlements/flows | Create a new cross-border settlement flow
*PaymentsCrossBorderSettlementApi* | [**delete_xb_settlement_config**](docs/apis/tags/PaymentsCrossBorderSettlementApi.md#delete_xb_settlement_config) | **delete** /payments/xb-settlements/configs/{configId} | Delete a cross-border settlement configuration
*PaymentsCrossBorderSettlementApi* | [**execute_xb_settlement_flow_action**](docs/apis/tags/PaymentsCrossBorderSettlementApi.md#execute_xb_settlement_flow_action) | **post** /payments/xb-settlements/flows/{flowId}/actions/execute | Execute cross-border settlement flow
*PaymentsCrossBorderSettlementApi* | [**get_xb_settlement_config_by_id**](docs/apis/tags/PaymentsCrossBorderSettlementApi.md#get_xb_settlement_config_by_id) | **get** /payments/xb-settlements/configs/{configId} | Get a specific cross-border settlement configuration
*PaymentsCrossBorderSettlementApi* | [**get_xb_settlement_configs**](docs/apis/tags/PaymentsCrossBorderSettlementApi.md#get_xb_settlement_configs) | **get** /payments/xb-settlements/configs | Get all the cross-border settlement configurations
*PaymentsCrossBorderSettlementApi* | [**get_xb_settlement_flow_by_id**](docs/apis/tags/PaymentsCrossBorderSettlementApi.md#get_xb_settlement_flow_by_id) | **get** /payments/xb-settlements/flows/{flowId} | Get specific cross-border settlement flow details
*PaymentsCrossBorderSettlementApi* | [**update_xb_settlement_config**](docs/apis/tags/PaymentsCrossBorderSettlementApi.md#update_xb_settlement_config) | **put** /payments/xb-settlements/configs/{configId} | Edit a cross-border settlement configuration
*PolicyEditorBetaApi* | [**get_active_policy**](docs/apis/tags/PolicyEditorBetaApi.md#get_active_policy) | **get** /tap/active_policy | Get the active policy and its validation
*PolicyEditorBetaApi* | [**get_draft**](docs/apis/tags/PolicyEditorBetaApi.md#get_draft) | **get** /tap/draft | Get the active draft
*PolicyEditorBetaApi* | [**publish_draft**](docs/apis/tags/PolicyEditorBetaApi.md#publish_draft) | **post** /tap/draft | Send publish request for a certain draft id
*PolicyEditorBetaApi* | [**publish_policy_rules**](docs/apis/tags/PolicyEditorBetaApi.md#publish_policy_rules) | **post** /tap/publish | Send publish request for a set of policy rules
*PolicyEditorBetaApi* | [**update_draft**](docs/apis/tags/PolicyEditorBetaApi.md#update_draft) | **put** /tap/draft | Update the draft with a new set of rules
*TransactionsApi* | [**cancel_transaction**](docs/apis/tags/TransactionsApi.md#cancel_transaction) | **post** /transactions/{txId}/cancel | Cancel a transaction
*TransactionsApi* | [**create_transaction**](docs/apis/tags/TransactionsApi.md#create_transaction) | **post** /transactions | Create a new transaction
*TransactionsApi* | [**drop_transaction**](docs/apis/tags/TransactionsApi.md#drop_transaction) | **post** /transactions/{txId}/drop | Drop ETH transaction by ID
*TransactionsApi* | [**estimate_network_fee**](docs/apis/tags/TransactionsApi.md#estimate_network_fee) | **get** /estimate_network_fee | Estimate the required fee for an asset
*TransactionsApi* | [**estimate_transaction_fee**](docs/apis/tags/TransactionsApi.md#estimate_transaction_fee) | **post** /transactions/estimate_fee | Estimate transaction fee
*TransactionsApi* | [**freeze_transaction**](docs/apis/tags/TransactionsApi.md#freeze_transaction) | **post** /transactions/{txId}/freeze | Freeze a transaction
*TransactionsApi* | [**get_transaction_by_external_id**](docs/apis/tags/TransactionsApi.md#get_transaction_by_external_id) | **get** /transactions/external_tx_id/{externalTxId}/ | Find a specific transaction by external transaction ID
*TransactionsApi* | [**get_transaction_by_id**](docs/apis/tags/TransactionsApi.md#get_transaction_by_id) | **get** /transactions/{txId} | Find a specific transaction by Fireblocks transaction ID
*TransactionsApi* | [**get_transactions**](docs/apis/tags/TransactionsApi.md#get_transactions) | **get** /transactions | List transaction history
*TransactionsApi* | [**set_confirmation_threshold_for_transaction**](docs/apis/tags/TransactionsApi.md#set_confirmation_threshold_for_transaction) | **post** /transactions/{txId}/set_confirmation_threshold | Set confirmation threshold by transaction ID
*TransactionsApi* | [**set_confirmation_threshold_for_transaction_by_hash**](docs/apis/tags/TransactionsApi.md#set_confirmation_threshold_for_transaction_by_hash) | **post** /txHash/{txHash}/set_confirmation_threshold | Set confirmation threshold by transaction hash
*TransactionsApi* | [**unfreeze_transaction**](docs/apis/tags/TransactionsApi.md#unfreeze_transaction) | **post** /transactions/{txId}/unfreeze | Unfreeze a transaction
*TransactionsApi* | [**validate_address**](docs/apis/tags/TransactionsApi.md#validate_address) | **get** /transactions/validate_address/{assetId}/{address} | Validate destination address
*TravelRuleBetaApi* | [**get_vaspby_did**](docs/apis/tags/TravelRuleBetaApi.md#get_vaspby_did) | **get** /screening/travel_rule/vasp/{did} | Get VASP details
*TravelRuleBetaApi* | [**get_vasps**](docs/apis/tags/TravelRuleBetaApi.md#get_vasps) | **get** /screening/travel_rule/vasp | Get All VASPs
*TravelRuleBetaApi* | [**travel_rule_api_controller_update_vasp**](docs/apis/tags/TravelRuleBetaApi.md#travel_rule_api_controller_update_vasp) | **put** /screeening/travel_rule/vasp/update | Add jsonDidKey to VASP details
*TravelRuleBetaApi* | [**validate_full_travel_rule_transaction**](docs/apis/tags/TravelRuleBetaApi.md#validate_full_travel_rule_transaction) | **post** /screening/travel_rule/transaction/validate/full | Validate Full Travel Rule Transaction
*TravelRuleBetaApi* | [**validate_travel_rule_transaction**](docs/apis/tags/TravelRuleBetaApi.md#validate_travel_rule_transaction) | **post** /screening/travel_rule/transaction/validate | Validate Travel Rule Transaction
*UsersApi* | [**get_users**](docs/apis/tags/UsersApi.md#get_users) | **get** /users | List users
*UsersGroupsBetaApi* | [**create_user_group**](docs/apis/tags/UsersGroupsBetaApi.md#create_user_group) | **post** /users_groups | Create users group
*UsersGroupsBetaApi* | [**delete_user_group**](docs/apis/tags/UsersGroupsBetaApi.md#delete_user_group) | **delete** /users_groups/{groupId} | Delete users group
*UsersGroupsBetaApi* | [**get_user_group**](docs/apis/tags/UsersGroupsBetaApi.md#get_user_group) | **get** /users_groups/{groupId} | Get users group
*UsersGroupsBetaApi* | [**get_user_groups**](docs/apis/tags/UsersGroupsBetaApi.md#get_user_groups) | **get** /users_groups | List users groups
*UsersGroupsBetaApi* | [**update_user_group**](docs/apis/tags/UsersGroupsBetaApi.md#update_user_group) | **put** /users_groups/{groupId} | Update users group
*VaultsApi* | [**activate_asset_for_vault_account**](docs/apis/tags/VaultsApi.md#activate_asset_for_vault_account) | **post** /vault/accounts/{vaultAccountId}/{assetId}/activate | Activate a wallet in a vault account
*VaultsApi* | [**create_legacy_address_for_vault_account_asset**](docs/apis/tags/VaultsApi.md#create_legacy_address_for_vault_account_asset) | **post** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId}/create_legacy | Convert a segwit address to legacy format
*VaultsApi* | [**create_vault_account**](docs/apis/tags/VaultsApi.md#create_vault_account) | **post** /vault/accounts | Create a new vault account
*VaultsApi* | [**create_vault_account_asset**](docs/apis/tags/VaultsApi.md#create_vault_account_asset) | **post** /vault/accounts/{vaultAccountId}/{assetId} | Create a new wallet
*VaultsApi* | [**create_vault_account_asset_address**](docs/apis/tags/VaultsApi.md#create_vault_account_asset_address) | **post** /vault/accounts/{vaultAccountId}/{assetId}/addresses | Create new asset deposit address
*VaultsApi* | [**get_asset_wallets**](docs/apis/tags/VaultsApi.md#get_asset_wallets) | **get** /vault/asset_wallets | List asset wallets (Paginated)
*VaultsApi* | [**get_max_spendable_amount**](docs/apis/tags/VaultsApi.md#get_max_spendable_amount) | **get** /vault/accounts/{vaultAccountId}/{assetId}/max_spendable_amount | Get the maximum spendable amount in a single transaction.
*VaultsApi* | [**get_paged_vault_accounts**](docs/apis/tags/VaultsApi.md#get_paged_vault_accounts) | **get** /vault/accounts_paged | List vault acounts (Paginated)
*VaultsApi* | [**get_public_key_info**](docs/apis/tags/VaultsApi.md#get_public_key_info) | **get** /vault/public_key_info/ | Get the public key information
*VaultsApi* | [**get_public_key_info_for_address**](docs/apis/tags/VaultsApi.md#get_public_key_info_for_address) | **get** /vault/accounts/{vaultAccountId}/{assetId}/{change}/{addressIndex}/public_key_info | Get the public key for a vault account
*VaultsApi* | [**get_vault_account_asset**](docs/apis/tags/VaultsApi.md#get_vault_account_asset) | **get** /vault/accounts/{vaultAccountId}/{assetId} | Get the asset balance for a vault account
*VaultsApi* | [**get_vault_account_asset_addresses**](docs/apis/tags/VaultsApi.md#get_vault_account_asset_addresses) | **get** /vault/accounts/{vaultAccountId}/{assetId}/addresses | Get asset addresses
*VaultsApi* | [**get_vault_account_asset_unspent_inputs**](docs/apis/tags/VaultsApi.md#get_vault_account_asset_unspent_inputs) | **get** /vault/accounts/{vaultAccountId}/{assetId}/unspent_inputs | Get UTXO unspent inputs information
*VaultsApi* | [**get_vault_account_by_id**](docs/apis/tags/VaultsApi.md#get_vault_account_by_id) | **get** /vault/accounts/{vaultAccountId} | Find a vault account by ID
*VaultsApi* | [**get_vault_accounts**](docs/apis/tags/VaultsApi.md#get_vault_accounts) | **get** /vault/accounts | List vault accounts
*VaultsApi* | [**get_vault_asset_by_id**](docs/apis/tags/VaultsApi.md#get_vault_asset_by_id) | **get** /vault/assets/{assetId} | Get vault balance by asset
*VaultsApi* | [**get_vault_assets**](docs/apis/tags/VaultsApi.md#get_vault_assets) | **get** /vault/assets | Get asset balance for chosen assets
*VaultsApi* | [**hide_vault_account**](docs/apis/tags/VaultsApi.md#hide_vault_account) | **post** /vault/accounts/{vaultAccountId}/hide | Hide a vault account in the console
*VaultsApi* | [**set_auto_fuel_for_vault_account**](docs/apis/tags/VaultsApi.md#set_auto_fuel_for_vault_account) | **post** /vault/accounts/{vaultAccountId}/set_auto_fuel | Turn autofueling on or off
*VaultsApi* | [**set_customer_ref_id_for_vault_account**](docs/apis/tags/VaultsApi.md#set_customer_ref_id_for_vault_account) | **post** /vault/accounts/{vaultAccountId}/set_customer_ref_id | Set an AML/KYT customer reference ID for a vault account
*VaultsApi* | [**set_customer_ref_id_for_vault_account_asset_address**](docs/apis/tags/VaultsApi.md#set_customer_ref_id_for_vault_account_asset_address) | **post** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId}/set_customer_ref_id | Assign AML customer reference ID
*VaultsApi* | [**unhide_vault_account**](docs/apis/tags/VaultsApi.md#unhide_vault_account) | **post** /vault/accounts/{vaultAccountId}/unhide | Unhide a vault account in the console
*VaultsApi* | [**update_vault_account**](docs/apis/tags/VaultsApi.md#update_vault_account) | **put** /vault/accounts/{vaultAccountId} | Rename a vault account
*VaultsApi* | [**update_vault_account_asset_address**](docs/apis/tags/VaultsApi.md#update_vault_account_asset_address) | **put** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId} | Update address description
*VaultsApi* | [**update_vault_account_asset_balance**](docs/apis/tags/VaultsApi.md#update_vault_account_asset_balance) | **post** /vault/accounts/{vaultAccountId}/{assetId}/balance | Refresh asset balance data
*Web3ConnectionsApi* | [**create**](docs/apis/tags/Web3ConnectionsApi.md#create) | **post** /connections/wc | Create a new Web3 connection.
*Web3ConnectionsApi* | [**get**](docs/apis/tags/Web3ConnectionsApi.md#get) | **get** /connections | List all open Web3 connections.
*Web3ConnectionsApi* | [**remove**](docs/apis/tags/Web3ConnectionsApi.md#remove) | **delete** /connections/wc/{id} | Remove an existing Web3 connection.
*Web3ConnectionsApi* | [**submit**](docs/apis/tags/Web3ConnectionsApi.md#submit) | **put** /connections/wc/{id} | Respond to a pending Web3 connection request.
*WebhooksApi* | [**resend_webhooks**](docs/apis/tags/WebhooksApi.md#resend_webhooks) | **post** /webhooks/resend | Resend failed webhooks
*WebhooksApi* | [**resend_webhooks_for_transaction**](docs/apis/tags/WebhooksApi.md#resend_webhooks_for_transaction) | **post** /webhooks/resend/{txId} | Resend failed webhooks for a transaction by ID

## Documentation For Models

 - [AddCollateralRequestBody](docs/models/AddCollateralRequestBody.md)
 - [AmlScreeningResult](docs/models/AmlScreeningResult.md)
 - [AmountAggregationTimePeriodMethod](docs/models/AmountAggregationTimePeriodMethod.md)
 - [AmountInfo](docs/models/AmountInfo.md)
 - [AssetTypeResponse](docs/models/AssetTypeResponse.md)
 - [AssetWallet](docs/models/AssetWallet.md)
 - [AuthorizationGroups](docs/models/AuthorizationGroups.md)
 - [AuthorizationInfo](docs/models/AuthorizationInfo.md)
 - [BlockInfo](docs/models/BlockInfo.md)
 - [CancelTransactionResponse](docs/models/CancelTransactionResponse.md)
 - [CollectionOwnershipResponse](docs/models/CollectionOwnershipResponse.md)
 - [ConfigChangeRequestStatus](docs/models/ConfigChangeRequestStatus.md)
 - [CreateAddressResponse](docs/models/CreateAddressResponse.md)
 - [CreateConnectionRequest](docs/models/CreateConnectionRequest.md)
 - [CreateConnectionResponse](docs/models/CreateConnectionResponse.md)
 - [CreateInternalTransferRequest](docs/models/CreateInternalTransferRequest.md)
 - [CreatePayoutRequest](docs/models/CreatePayoutRequest.md)
 - [CreateTransactionResponse](docs/models/CreateTransactionResponse.md)
 - [CreateUsersGroupResponse](docs/models/CreateUsersGroupResponse.md)
 - [CreateVaultAssetResponse](docs/models/CreateVaultAssetResponse.md)
 - [CustomCryptoRoutingDest](docs/models/CustomCryptoRoutingDest.md)
 - [CustomFiatRoutingDest](docs/models/CustomFiatRoutingDest.md)
 - [DefaultNetworkRoutingDest](docs/models/DefaultNetworkRoutingDest.md)
 - [DestinationTransferPeerPath](docs/models/DestinationTransferPeerPath.md)
 - [DestinationTransferPeerPathResponse](docs/models/DestinationTransferPeerPathResponse.md)
 - [DispatchPayoutResponse](docs/models/DispatchPayoutResponse.md)
 - [DraftResponse](docs/models/DraftResponse.md)
 - [DraftReviewAndValidationResponse](docs/models/DraftReviewAndValidationResponse.md)
 - [DropTransactionRequest](docs/models/DropTransactionRequest.md)
 - [DropTransactionResponse](docs/models/DropTransactionResponse.md)
 - [Error](docs/models/Error.md)
 - [ErrorResponse](docs/models/ErrorResponse.md)
 - [EstimatedNetworkFeeResponse](docs/models/EstimatedNetworkFeeResponse.md)
 - [EstimatedTransactionFeeResponse](docs/models/EstimatedTransactionFeeResponse.md)
 - [ExchangeAccount](docs/models/ExchangeAccount.md)
 - [ExchangeAsset](docs/models/ExchangeAsset.md)
 - [ExchangeTradingAccount](docs/models/ExchangeTradingAccount.md)
 - [ExchangeType](docs/models/ExchangeType.md)
 - [ExternalWalletAsset](docs/models/ExternalWalletAsset.md)
 - [FeeInfo](docs/models/FeeInfo.md)
 - [FiatAccount](docs/models/FiatAccount.md)
 - [FiatAccountType](docs/models/FiatAccountType.md)
 - [FiatAsset](docs/models/FiatAsset.md)
 - [FreezeTransactionResponse](docs/models/FreezeTransactionResponse.md)
 - [GasStationConfiguration](docs/models/GasStationConfiguration.md)
 - [GasStationPropertiesResponse](docs/models/GasStationPropertiesResponse.md)
 - [GetConnectionsResponse](docs/models/GetConnectionsResponse.md)
 - [GetSettlementResponse](docs/models/GetSettlementResponse.md)
 - [GetTransactionOperation](docs/models/GetTransactionOperation.md)
 - [GetUsersResponse](docs/models/GetUsersResponse.md)
 - [InstructionAmount](docs/models/InstructionAmount.md)
 - [MediaEntityResponse](docs/models/MediaEntityResponse.md)
 - [Ncw](docs/models/Ncw.md)
 - [NetworkChannel](docs/models/NetworkChannel.md)
 - [NetworkConnection](docs/models/NetworkConnection.md)
 - [NetworkConnectionResponse](docs/models/NetworkConnectionResponse.md)
 - [NetworkConnectionRoutingPolicy](docs/models/NetworkConnectionRoutingPolicy.md)
 - [NetworkFee](docs/models/NetworkFee.md)
 - [NetworkId](docs/models/NetworkId.md)
 - [NetworkIdResponse](docs/models/NetworkIdResponse.md)
 - [NetworkIdRoutingPolicy](docs/models/NetworkIdRoutingPolicy.md)
 - [NetworkRecord](docs/models/NetworkRecord.md)
 - [NoneNetworkRoutingDest](docs/models/NoneNetworkRoutingDest.md)
 - [OneTimeAddress](docs/models/OneTimeAddress.md)
 - [PaginatedAssetWalletResponse](docs/models/PaginatedAssetWalletResponse.md)
 - [Paging](docs/models/Paging.md)
 - [PayeeAccount](docs/models/PayeeAccount.md)
 - [PayeeAccountResponse](docs/models/PayeeAccountResponse.md)
 - [PayeeAccountType](docs/models/PayeeAccountType.md)
 - [PaymentAccount](docs/models/PaymentAccount.md)
 - [PaymentAccountResponse](docs/models/PaymentAccountResponse.md)
 - [PaymentAccountType](docs/models/PaymentAccountType.md)
 - [PayoutInitMethod](docs/models/PayoutInitMethod.md)
 - [PayoutInstruction](docs/models/PayoutInstruction.md)
 - [PayoutInstructionResponse](docs/models/PayoutInstructionResponse.md)
 - [PayoutInstructionState](docs/models/PayoutInstructionState.md)
 - [PayoutResponse](docs/models/PayoutResponse.md)
 - [PayoutState](docs/models/PayoutState.md)
 - [PayoutStatus](docs/models/PayoutStatus.md)
 - [PolicyAndValidationResponse](docs/models/PolicyAndValidationResponse.md)
 - [PolicyCheckResult](docs/models/PolicyCheckResult.md)
 - [PolicyMetadata](docs/models/PolicyMetadata.md)
 - [PolicyResponse](docs/models/PolicyResponse.md)
 - [PolicyRule](docs/models/PolicyRule.md)
 - [PolicyRuleCheckResult](docs/models/PolicyRuleCheckResult.md)
 - [PolicyRuleError](docs/models/PolicyRuleError.md)
 - [PolicySrcOrDestId](docs/models/PolicySrcOrDestId.md)
 - [PolicySrcOrDestSubType](docs/models/PolicySrcOrDestSubType.md)
 - [PolicySrcOrDestType](docs/models/PolicySrcOrDestType.md)
 - [PolicyStatus](docs/models/PolicyStatus.md)
 - [PolicyValidation](docs/models/PolicyValidation.md)
 - [PublicKeyInformation](docs/models/PublicKeyInformation.md)
 - [PublishResult](docs/models/PublishResult.md)
 - [RemoveCollateralRequestBody](docs/models/RemoveCollateralRequestBody.md)
 - [RequestOptions](docs/models/RequestOptions.md)
 - [ResendWebhooksResponse](docs/models/ResendWebhooksResponse.md)
 - [RespondToConnectionRequest](docs/models/RespondToConnectionRequest.md)
 - [RewardInfo](docs/models/RewardInfo.md)
 - [RewardsInfo](docs/models/RewardsInfo.md)
 - [SessionDTO](docs/models/SessionDTO.md)
 - [SessionMetadata](docs/models/SessionMetadata.md)
 - [SetConfirmationsThresholdRequest](docs/models/SetConfirmationsThresholdRequest.md)
 - [SetConfirmationsThresholdResponse](docs/models/SetConfirmationsThresholdResponse.md)
 - [SettlementRequestBody](docs/models/SettlementRequestBody.md)
 - [SettlementResponse](docs/models/SettlementResponse.md)
 - [SignedMessage](docs/models/SignedMessage.md)
 - [SourceTransferPeerPathResponse](docs/models/SourceTransferPeerPathResponse.md)
 - [SystemMessageInfo](docs/models/SystemMessageInfo.md)
 - [Term](docs/models/Term.md)
 - [ToCollateralTransaction](docs/models/ToCollateralTransaction.md)
 - [ToExchangeTransaction](docs/models/ToExchangeTransaction.md)
 - [TokenCollectionResponse](docs/models/TokenCollectionResponse.md)
 - [TokenOwnershipResponse](docs/models/TokenOwnershipResponse.md)
 - [TokenResponse](docs/models/TokenResponse.md)
 - [TradingAccountType](docs/models/TradingAccountType.md)
 - [Transaction](docs/models/Transaction.md)
 - [TransactionFee](docs/models/TransactionFee.md)
 - [TransactionOperation](docs/models/TransactionOperation.md)
 - [TransactionRequest](docs/models/TransactionRequest.md)
 - [TransactionRequestDestination](docs/models/TransactionRequestDestination.md)
 - [TransactionResponse](docs/models/TransactionResponse.md)
 - [TransactionResponseDestination](docs/models/TransactionResponseDestination.md)
 - [TransferPeerPath](docs/models/TransferPeerPath.md)
 - [TravelRuleAddress](docs/models/TravelRuleAddress.md)
 - [TravelRuleGetAllVASPsResponse](docs/models/TravelRuleGetAllVASPsResponse.md)
 - [TravelRuleIssuer](docs/models/TravelRuleIssuer.md)
 - [TravelRuleIssuers](docs/models/TravelRuleIssuers.md)
 - [TravelRuleOwnershipProof](docs/models/TravelRuleOwnershipProof.md)
 - [TravelRulePiiIVMS](docs/models/TravelRulePiiIVMS.md)
 - [TravelRuleTransactionBlockchainInfo](docs/models/TravelRuleTransactionBlockchainInfo.md)
 - [TravelRuleUpdateVASPDetails](docs/models/TravelRuleUpdateVASPDetails.md)
 - [TravelRuleVASP](docs/models/TravelRuleVASP.md)
 - [TravelRuleValidateFullTransactionRequest](docs/models/TravelRuleValidateFullTransactionRequest.md)
 - [TravelRuleValidateTransactionRequest](docs/models/TravelRuleValidateTransactionRequest.md)
 - [TravelRuleValidateTransactionResponse](docs/models/TravelRuleValidateTransactionResponse.md)
 - [UnfreezeTransactionResponse](docs/models/UnfreezeTransactionResponse.md)
 - [UnmanagedWallet](docs/models/UnmanagedWallet.md)
 - [UnsignedMessage](docs/models/UnsignedMessage.md)
 - [UnspentInput](docs/models/UnspentInput.md)
 - [UnspentInputsResponse](docs/models/UnspentInputsResponse.md)
 - [UpdateTokenOwnershipStatusDto](docs/models/UpdateTokenOwnershipStatusDto.md)
 - [UserGroupCreateRequest](docs/models/UserGroupCreateRequest.md)
 - [UserGroupCreateResponse](docs/models/UserGroupCreateResponse.md)
 - [UserGroupUpdateRequest](docs/models/UserGroupUpdateRequest.md)
 - [UserResponse](docs/models/UserResponse.md)
 - [UsersGroupResponse](docs/models/UsersGroupResponse.md)
 - [UsersGroupsResponse](docs/models/UsersGroupsResponse.md)
 - [ValidateAddressResponse](docs/models/ValidateAddressResponse.md)
 - [VaultAccount](docs/models/VaultAccount.md)
 - [VaultAccountsPagedResponse](docs/models/VaultAccountsPagedResponse.md)
 - [VaultAsset](docs/models/VaultAsset.md)
 - [VaultWalletAddress](docs/models/VaultWalletAddress.md)
 - [WalletAsset](docs/models/WalletAsset.md)
 - [WalletAssetAdditionalInfo](docs/models/WalletAssetAdditionalInfo.md)
 - [XBSettlementAsset](docs/models/XBSettlementAsset.md)
 - [XBSettlementAssetID](docs/models/XBSettlementAssetID.md)
 - [XBSettlementConfigCreationRequestBody](docs/models/XBSettlementConfigCreationRequestBody.md)
 - [XBSettlementConfigCreationResponse](docs/models/XBSettlementConfigCreationResponse.md)
 - [XBSettlementConfigDeletionResponse](docs/models/XBSettlementConfigDeletionResponse.md)
 - [XBSettlementConfigEditRequestBody](docs/models/XBSettlementConfigEditRequestBody.md)
 - [XBSettlementConfigEditResponse](docs/models/XBSettlementConfigEditResponse.md)
 - [XBSettlementConfigId](docs/models/XBSettlementConfigId.md)
 - [XBSettlementConfigModel](docs/models/XBSettlementConfigModel.md)
 - [XBSettlementConfigStep](docs/models/XBSettlementConfigStep.md)
 - [XBSettlementConfigStepsRecord](docs/models/XBSettlementConfigStepsRecord.md)
 - [XBSettlementConversionSlippageBasisPoints](docs/models/XBSettlementConversionSlippageBasisPoints.md)
 - [XBSettlementCorridorId](docs/models/XBSettlementCorridorId.md)
 - [XBSettlementCreateFlowRequestBody](docs/models/XBSettlementCreateFlowRequestBody.md)
 - [XBSettlementCreateFlowResponse](docs/models/XBSettlementCreateFlowResponse.md)
 - [XBSettlementCryptoAsset](docs/models/XBSettlementCryptoAsset.md)
 - [XBSettlementFiatAsset](docs/models/XBSettlementFiatAsset.md)
 - [XBSettlementFlowExecutionModel](docs/models/XBSettlementFlowExecutionModel.md)
 - [XBSettlementFlowExecutionRequestBody](docs/models/XBSettlementFlowExecutionRequestBody.md)
 - [XBSettlementFlowExecutionResponse](docs/models/XBSettlementFlowExecutionResponse.md)
 - [XBSettlementFlowExecutionStatus](docs/models/XBSettlementFlowExecutionStatus.md)
 - [XBSettlementFlowExecutionStep](docs/models/XBSettlementFlowExecutionStep.md)
 - [XBSettlementFlowExecutionStepStatus](docs/models/XBSettlementFlowExecutionStepStatus.md)
 - [XBSettlementFlowPreviewModel](docs/models/XBSettlementFlowPreviewModel.md)
 - [XBSettlementFlowSelectedConversionSlippageReason](docs/models/XBSettlementFlowSelectedConversionSlippageReason.md)
 - [XBSettlementFlowSetupStep](docs/models/XBSettlementFlowSetupStep.md)
 - [XBSettlementFlowStepsExecutionRecord](docs/models/XBSettlementFlowStepsExecutionRecord.md)
 - [XBSettlementFlowStepsRecord](docs/models/XBSettlementFlowStepsRecord.md)
 - [XBSettlementGetAllConfigsResponse](docs/models/XBSettlementGetAllConfigsResponse.md)
 - [XBSettlementGetConfigResponse](docs/models/XBSettlementGetConfigResponse.md)
 - [XBSettlementGetFlowResponse](docs/models/XBSettlementGetFlowResponse.md)
 - [XBSettlementStepType](docs/models/XBSettlementStepType.md)

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="bearerTokenAuth"></a>
### bearerTokenAuth

- **Type**: Bearer authentication (JWT)

<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Author

support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com
support@fireblocks.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in fireblocks_client.apis and fireblocks_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from fireblocks_client.apis.default_api import DefaultApi`
- `from fireblocks_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import fireblocks_client
from fireblocks_client.apis import *
from fireblocks_client.models import *
```
