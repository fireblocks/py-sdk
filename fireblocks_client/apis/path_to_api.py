import typing_extensions

from fireblocks_client.paths import PathValues
from fireblocks_client.apis.paths.vault_accounts import VaultAccounts
from fireblocks_client.apis.paths.vault_accounts_paged import VaultAccountsPaged
from fireblocks_client.apis.paths.vault_accounts_vault_account_id import VaultAccountsVaultAccountId
from fireblocks_client.apis.paths.vault_asset_wallets import VaultAssetWallets
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_hide import VaultAccountsVaultAccountIdHide
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_unhide import VaultAccountsVaultAccountIdUnhide
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_asset_id_activate import VaultAccountsVaultAccountIdAssetIdActivate
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_set_customer_ref_id import VaultAccountsVaultAccountIdSetCustomerRefId
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_set_auto_fuel import VaultAccountsVaultAccountIdSetAutoFuel
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_asset_id import VaultAccountsVaultAccountIdAssetId
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_asset_id_balance import VaultAccountsVaultAccountIdAssetIdBalance
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_asset_id_addresses import VaultAccountsVaultAccountIdAssetIdAddresses
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_asset_id_max_spendable_amount import VaultAccountsVaultAccountIdAssetIdMaxSpendableAmount
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_asset_id_addresses_address_id import VaultAccountsVaultAccountIdAssetIdAddressesAddressId
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_asset_id_addresses_address_id_set_customer_ref_id import VaultAccountsVaultAccountIdAssetIdAddressesAddressIdSetCustomerRefId
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_asset_id_addresses_address_id_create_legacy import VaultAccountsVaultAccountIdAssetIdAddressesAddressIdCreateLegacy
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_asset_id_unspent_inputs import VaultAccountsVaultAccountIdAssetIdUnspentInputs
from fireblocks_client.apis.paths.vault_public_key_info_ import VaultPublicKeyInfo
from fireblocks_client.apis.paths.vault_accounts_vault_account_id_asset_id_change_address_index_public_key_info import VaultAccountsVaultAccountIdAssetIdChangeAddressIndexPublicKeyInfo
from fireblocks_client.apis.paths.vault_assets import VaultAssets
from fireblocks_client.apis.paths.vault_assets_asset_id import VaultAssetsAssetId
from fireblocks_client.apis.paths.exchange_accounts import ExchangeAccounts
from fireblocks_client.apis.paths.exchange_accounts_exchange_account_id import ExchangeAccountsExchangeAccountId
from fireblocks_client.apis.paths.exchange_accounts_exchange_account_id_internal_transfer import ExchangeAccountsExchangeAccountIdInternalTransfer
from fireblocks_client.apis.paths.exchange_accounts_exchange_account_id_convert import ExchangeAccountsExchangeAccountIdConvert
from fireblocks_client.apis.paths.exchange_accounts_exchange_account_id_asset_id import ExchangeAccountsExchangeAccountIdAssetId
from fireblocks_client.apis.paths.fiat_accounts import FiatAccounts
from fireblocks_client.apis.paths.fiat_accounts_account_id import FiatAccountsAccountId
from fireblocks_client.apis.paths.fiat_accounts_account_id_redeem_to_linked_dda import FiatAccountsAccountIdRedeemToLinkedDda
from fireblocks_client.apis.paths.fiat_accounts_account_id_deposit_from_linked_dda import FiatAccountsAccountIdDepositFromLinkedDda
from fireblocks_client.apis.paths.network_connections import NetworkConnections
from fireblocks_client.apis.paths.network_connections_connection_id_set_routing_policy import NetworkConnectionsConnectionIdSetRoutingPolicy
from fireblocks_client.apis.paths.network_connections_connection_id_is_third_party_routing_asset_type import NetworkConnectionsConnectionIdIsThirdPartyRoutingAssetType
from fireblocks_client.apis.paths.network_connections_connection_id import NetworkConnectionsConnectionId
from fireblocks_client.apis.paths.network_ids import NetworkIds
from fireblocks_client.apis.paths.network_ids_network_id import NetworkIdsNetworkId
from fireblocks_client.apis.paths.network_ids_network_id_set_routing_policy import NetworkIdsNetworkIdSetRoutingPolicy
from fireblocks_client.apis.paths.network_ids_network_id_set_discoverability import NetworkIdsNetworkIdSetDiscoverability
from fireblocks_client.apis.paths.network_ids_network_id_set_name import NetworkIdsNetworkIdSetName
from fireblocks_client.apis.paths.internal_wallets import InternalWallets
from fireblocks_client.apis.paths.internal_wallets_wallet_id import InternalWalletsWalletId
from fireblocks_client.apis.paths.internal_wallets_wallet_id_set_customer_ref_id import InternalWalletsWalletIdSetCustomerRefId
from fireblocks_client.apis.paths.internal_wallets_wallet_id_asset_id import InternalWalletsWalletIdAssetId
from fireblocks_client.apis.paths.external_wallets import ExternalWallets
from fireblocks_client.apis.paths.external_wallets_wallet_id import ExternalWalletsWalletId
from fireblocks_client.apis.paths.external_wallets_wallet_id_set_customer_ref_id import ExternalWalletsWalletIdSetCustomerRefId
from fireblocks_client.apis.paths.external_wallets_wallet_id_asset_id import ExternalWalletsWalletIdAssetId
from fireblocks_client.apis.paths.contracts import Contracts
from fireblocks_client.apis.paths.contracts_contract_id import ContractsContractId
from fireblocks_client.apis.paths.contracts_contract_id_asset_id import ContractsContractIdAssetId
from fireblocks_client.apis.paths.supported_assets import SupportedAssets
from fireblocks_client.apis.paths.transactions import Transactions
from fireblocks_client.apis.paths.transactions_estimate_fee import TransactionsEstimateFee
from fireblocks_client.apis.paths.transactions_tx_id import TransactionsTxId
from fireblocks_client.apis.paths.transactions_external_tx_id_external_tx_id_ import TransactionsExternalTxIdExternalTxId
from fireblocks_client.apis.paths.transactions_tx_id_set_confirmation_threshold import TransactionsTxIdSetConfirmationThreshold
from fireblocks_client.apis.paths.transactions_tx_id_drop import TransactionsTxIdDrop
from fireblocks_client.apis.paths.transactions_tx_id_cancel import TransactionsTxIdCancel
from fireblocks_client.apis.paths.transactions_tx_id_freeze import TransactionsTxIdFreeze
from fireblocks_client.apis.paths.transactions_tx_id_unfreeze import TransactionsTxIdUnfreeze
from fireblocks_client.apis.paths.transactions_validate_address_asset_id_address import TransactionsValidateAddressAssetIdAddress
from fireblocks_client.apis.paths.tx_hash_tx_hash_set_confirmation_threshold import TxHashTxHashSetConfirmationThreshold
from fireblocks_client.apis.paths.estimate_network_fee import EstimateNetworkFee
from fireblocks_client.apis.paths.payments_xb_settlements_configs import PaymentsXbSettlementsConfigs
from fireblocks_client.apis.paths.payments_xb_settlements_configs_config_id import PaymentsXbSettlementsConfigsConfigId
from fireblocks_client.apis.paths.payments_xb_settlements_flows import PaymentsXbSettlementsFlows
from fireblocks_client.apis.paths.payments_xb_settlements_flows_flow_id import PaymentsXbSettlementsFlowsFlowId
from fireblocks_client.apis.paths.payments_xb_settlements_flows_flow_id_actions_execute import PaymentsXbSettlementsFlowsFlowIdActionsExecute
from fireblocks_client.apis.paths.payments_payout import PaymentsPayout
from fireblocks_client.apis.paths.payments_payout_payout_id_actions_execute import PaymentsPayoutPayoutIdActionsExecute
from fireblocks_client.apis.paths.payments_payout_payout_id import PaymentsPayoutPayoutId
from fireblocks_client.apis.paths.gas_station import GasStation
from fireblocks_client.apis.paths.gas_station_asset_id import GasStationAssetId
from fireblocks_client.apis.paths.gas_station_configuration import GasStationConfiguration
from fireblocks_client.apis.paths.gas_station_configuration_asset_id import GasStationConfigurationAssetId
from fireblocks_client.apis.paths.users import Users
from fireblocks_client.apis.paths.audits import Audits
from fireblocks_client.apis.paths.off_exchange_add import OffExchangeAdd
from fireblocks_client.apis.paths.off_exchange_remove import OffExchangeRemove
from fireblocks_client.apis.paths.off_exchange_settlements_trader import OffExchangeSettlementsTrader
from fireblocks_client.apis.paths.off_exchange_settlements_transactions import OffExchangeSettlementsTransactions
from fireblocks_client.apis.paths.off_exchange_collateral_accounts_main_exchange_account_id import OffExchangeCollateralAccountsMainExchangeAccountId
from fireblocks_client.apis.paths.webhooks_resend import WebhooksResend
from fireblocks_client.apis.paths.webhooks_resend_tx_id import WebhooksResendTxId
from fireblocks_client.apis.paths.nfts_ownership_tokens import NftsOwnershipTokens
from fireblocks_client.apis.paths.nfts_ownership_collections import NftsOwnershipCollections
from fireblocks_client.apis.paths.nfts_tokens_id import NftsTokensId
from fireblocks_client.apis.paths.nfts_tokens import NftsTokens
from fireblocks_client.apis.paths.nfts_ownership_tokens_id_status import NftsOwnershipTokensIdStatus
from fireblocks_client.apis.paths.connections import Connections
from fireblocks_client.apis.paths.connections_wc import ConnectionsWc
from fireblocks_client.apis.paths.connections_wc_id import ConnectionsWcId
from fireblocks_client.apis.paths.screening_travel_rule_transaction_validate import ScreeningTravelRuleTransactionValidate
from fireblocks_client.apis.paths.screening_travel_rule_transaction_validate_full import ScreeningTravelRuleTransactionValidateFull
from fireblocks_client.apis.paths.screening_travel_rule_vasp_did import ScreeningTravelRuleVaspDid
from fireblocks_client.apis.paths.screening_travel_rule_vasp import ScreeningTravelRuleVasp
from fireblocks_client.apis.paths.screeening_travel_rule_vasp_update import ScreeeningTravelRuleVaspUpdate
from fireblocks_client.apis.paths.tap_active_policy import TapActivePolicy
from fireblocks_client.apis.paths.tap_draft import TapDraft
from fireblocks_client.apis.paths.tap_publish import TapPublish

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.VAULT_ACCOUNTS: VaultAccounts,
        PathValues.VAULT_ACCOUNTS_PAGED: VaultAccountsPaged,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID: VaultAccountsVaultAccountId,
        PathValues.VAULT_ASSET_WALLETS: VaultAssetWallets,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_HIDE: VaultAccountsVaultAccountIdHide,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_UNHIDE: VaultAccountsVaultAccountIdUnhide,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_ACTIVATE: VaultAccountsVaultAccountIdAssetIdActivate,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_SET_CUSTOMER_REF_ID: VaultAccountsVaultAccountIdSetCustomerRefId,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_SET_AUTO_FUEL: VaultAccountsVaultAccountIdSetAutoFuel,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID: VaultAccountsVaultAccountIdAssetId,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_BALANCE: VaultAccountsVaultAccountIdAssetIdBalance,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_ADDRESSES: VaultAccountsVaultAccountIdAssetIdAddresses,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_MAX_SPENDABLE_AMOUNT: VaultAccountsVaultAccountIdAssetIdMaxSpendableAmount,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_ADDRESSES_ADDRESS_ID: VaultAccountsVaultAccountIdAssetIdAddressesAddressId,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_ADDRESSES_ADDRESS_ID_SET_CUSTOMER_REF_ID: VaultAccountsVaultAccountIdAssetIdAddressesAddressIdSetCustomerRefId,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_ADDRESSES_ADDRESS_ID_CREATE_LEGACY: VaultAccountsVaultAccountIdAssetIdAddressesAddressIdCreateLegacy,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_UNSPENT_INPUTS: VaultAccountsVaultAccountIdAssetIdUnspentInputs,
        PathValues.VAULT_PUBLIC_KEY_INFO_: VaultPublicKeyInfo,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_CHANGE_ADDRESS_INDEX_PUBLIC_KEY_INFO: VaultAccountsVaultAccountIdAssetIdChangeAddressIndexPublicKeyInfo,
        PathValues.VAULT_ASSETS: VaultAssets,
        PathValues.VAULT_ASSETS_ASSET_ID: VaultAssetsAssetId,
        PathValues.EXCHANGE_ACCOUNTS: ExchangeAccounts,
        PathValues.EXCHANGE_ACCOUNTS_EXCHANGE_ACCOUNT_ID: ExchangeAccountsExchangeAccountId,
        PathValues.EXCHANGE_ACCOUNTS_EXCHANGE_ACCOUNT_ID_INTERNAL_TRANSFER: ExchangeAccountsExchangeAccountIdInternalTransfer,
        PathValues.EXCHANGE_ACCOUNTS_EXCHANGE_ACCOUNT_ID_CONVERT: ExchangeAccountsExchangeAccountIdConvert,
        PathValues.EXCHANGE_ACCOUNTS_EXCHANGE_ACCOUNT_ID_ASSET_ID: ExchangeAccountsExchangeAccountIdAssetId,
        PathValues.FIAT_ACCOUNTS: FiatAccounts,
        PathValues.FIAT_ACCOUNTS_ACCOUNT_ID: FiatAccountsAccountId,
        PathValues.FIAT_ACCOUNTS_ACCOUNT_ID_REDEEM_TO_LINKED_DDA: FiatAccountsAccountIdRedeemToLinkedDda,
        PathValues.FIAT_ACCOUNTS_ACCOUNT_ID_DEPOSIT_FROM_LINKED_DDA: FiatAccountsAccountIdDepositFromLinkedDda,
        PathValues.NETWORK_CONNECTIONS: NetworkConnections,
        PathValues.NETWORK_CONNECTIONS_CONNECTION_ID_SET_ROUTING_POLICY: NetworkConnectionsConnectionIdSetRoutingPolicy,
        PathValues.NETWORK_CONNECTIONS_CONNECTION_ID_IS_THIRD_PARTY_ROUTING_ASSET_TYPE: NetworkConnectionsConnectionIdIsThirdPartyRoutingAssetType,
        PathValues.NETWORK_CONNECTIONS_CONNECTION_ID: NetworkConnectionsConnectionId,
        PathValues.NETWORK_IDS: NetworkIds,
        PathValues.NETWORK_IDS_NETWORK_ID: NetworkIdsNetworkId,
        PathValues.NETWORK_IDS_NETWORK_ID_SET_ROUTING_POLICY: NetworkIdsNetworkIdSetRoutingPolicy,
        PathValues.NETWORK_IDS_NETWORK_ID_SET_DISCOVERABILITY: NetworkIdsNetworkIdSetDiscoverability,
        PathValues.NETWORK_IDS_NETWORK_ID_SET_NAME: NetworkIdsNetworkIdSetName,
        PathValues.INTERNAL_WALLETS: InternalWallets,
        PathValues.INTERNAL_WALLETS_WALLET_ID: InternalWalletsWalletId,
        PathValues.INTERNAL_WALLETS_WALLET_ID_SET_CUSTOMER_REF_ID: InternalWalletsWalletIdSetCustomerRefId,
        PathValues.INTERNAL_WALLETS_WALLET_ID_ASSET_ID: InternalWalletsWalletIdAssetId,
        PathValues.EXTERNAL_WALLETS: ExternalWallets,
        PathValues.EXTERNAL_WALLETS_WALLET_ID: ExternalWalletsWalletId,
        PathValues.EXTERNAL_WALLETS_WALLET_ID_SET_CUSTOMER_REF_ID: ExternalWalletsWalletIdSetCustomerRefId,
        PathValues.EXTERNAL_WALLETS_WALLET_ID_ASSET_ID: ExternalWalletsWalletIdAssetId,
        PathValues.CONTRACTS: Contracts,
        PathValues.CONTRACTS_CONTRACT_ID: ContractsContractId,
        PathValues.CONTRACTS_CONTRACT_ID_ASSET_ID: ContractsContractIdAssetId,
        PathValues.SUPPORTED_ASSETS: SupportedAssets,
        PathValues.TRANSACTIONS: Transactions,
        PathValues.TRANSACTIONS_ESTIMATE_FEE: TransactionsEstimateFee,
        PathValues.TRANSACTIONS_TX_ID: TransactionsTxId,
        PathValues.TRANSACTIONS_EXTERNAL_TX_ID_EXTERNAL_TX_ID_: TransactionsExternalTxIdExternalTxId,
        PathValues.TRANSACTIONS_TX_ID_SET_CONFIRMATION_THRESHOLD: TransactionsTxIdSetConfirmationThreshold,
        PathValues.TRANSACTIONS_TX_ID_DROP: TransactionsTxIdDrop,
        PathValues.TRANSACTIONS_TX_ID_CANCEL: TransactionsTxIdCancel,
        PathValues.TRANSACTIONS_TX_ID_FREEZE: TransactionsTxIdFreeze,
        PathValues.TRANSACTIONS_TX_ID_UNFREEZE: TransactionsTxIdUnfreeze,
        PathValues.TRANSACTIONS_VALIDATE_ADDRESS_ASSET_ID_ADDRESS: TransactionsValidateAddressAssetIdAddress,
        PathValues.TX_HASH_TX_HASH_SET_CONFIRMATION_THRESHOLD: TxHashTxHashSetConfirmationThreshold,
        PathValues.ESTIMATE_NETWORK_FEE: EstimateNetworkFee,
        PathValues.PAYMENTS_XBSETTLEMENTS_CONFIGS: PaymentsXbSettlementsConfigs,
        PathValues.PAYMENTS_XBSETTLEMENTS_CONFIGS_CONFIG_ID: PaymentsXbSettlementsConfigsConfigId,
        PathValues.PAYMENTS_XBSETTLEMENTS_FLOWS: PaymentsXbSettlementsFlows,
        PathValues.PAYMENTS_XBSETTLEMENTS_FLOWS_FLOW_ID: PaymentsXbSettlementsFlowsFlowId,
        PathValues.PAYMENTS_XBSETTLEMENTS_FLOWS_FLOW_ID_ACTIONS_EXECUTE: PaymentsXbSettlementsFlowsFlowIdActionsExecute,
        PathValues.PAYMENTS_PAYOUT: PaymentsPayout,
        PathValues.PAYMENTS_PAYOUT_PAYOUT_ID_ACTIONS_EXECUTE: PaymentsPayoutPayoutIdActionsExecute,
        PathValues.PAYMENTS_PAYOUT_PAYOUT_ID: PaymentsPayoutPayoutId,
        PathValues.GAS_STATION: GasStation,
        PathValues.GAS_STATION_ASSET_ID: GasStationAssetId,
        PathValues.GAS_STATION_CONFIGURATION: GasStationConfiguration,
        PathValues.GAS_STATION_CONFIGURATION_ASSET_ID: GasStationConfigurationAssetId,
        PathValues.USERS: Users,
        PathValues.AUDITS: Audits,
        PathValues.OFF_EXCHANGE_ADD: OffExchangeAdd,
        PathValues.OFF_EXCHANGE_REMOVE: OffExchangeRemove,
        PathValues.OFF_EXCHANGE_SETTLEMENTS_TRADER: OffExchangeSettlementsTrader,
        PathValues.OFF_EXCHANGE_SETTLEMENTS_TRANSACTIONS: OffExchangeSettlementsTransactions,
        PathValues.OFF_EXCHANGE_COLLATERAL_ACCOUNTS_MAIN_EXCHANGE_ACCOUNT_ID: OffExchangeCollateralAccountsMainExchangeAccountId,
        PathValues.WEBHOOKS_RESEND: WebhooksResend,
        PathValues.WEBHOOKS_RESEND_TX_ID: WebhooksResendTxId,
        PathValues.NFTS_OWNERSHIP_TOKENS: NftsOwnershipTokens,
        PathValues.NFTS_OWNERSHIP_COLLECTIONS: NftsOwnershipCollections,
        PathValues.NFTS_TOKENS_ID: NftsTokensId,
        PathValues.NFTS_TOKENS: NftsTokens,
        PathValues.NFTS_OWNERSHIP_TOKENS_ID_STATUS: NftsOwnershipTokensIdStatus,
        PathValues.CONNECTIONS: Connections,
        PathValues.CONNECTIONS_WC: ConnectionsWc,
        PathValues.CONNECTIONS_WC_ID: ConnectionsWcId,
        PathValues.SCREENING_TRAVEL_RULE_TRANSACTION_VALIDATE: ScreeningTravelRuleTransactionValidate,
        PathValues.SCREENING_TRAVEL_RULE_TRANSACTION_VALIDATE_FULL: ScreeningTravelRuleTransactionValidateFull,
        PathValues.SCREENING_TRAVEL_RULE_VASP_DID: ScreeningTravelRuleVaspDid,
        PathValues.SCREENING_TRAVEL_RULE_VASP: ScreeningTravelRuleVasp,
        PathValues.SCREEENING_TRAVEL_RULE_VASP_UPDATE: ScreeeningTravelRuleVaspUpdate,
        PathValues.TAP_ACTIVE_POLICY: TapActivePolicy,
        PathValues.TAP_DRAFT: TapDraft,
        PathValues.TAP_PUBLISH: TapPublish,
    }
)

path_to_api = PathToApi(
    {
        PathValues.VAULT_ACCOUNTS: VaultAccounts,
        PathValues.VAULT_ACCOUNTS_PAGED: VaultAccountsPaged,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID: VaultAccountsVaultAccountId,
        PathValues.VAULT_ASSET_WALLETS: VaultAssetWallets,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_HIDE: VaultAccountsVaultAccountIdHide,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_UNHIDE: VaultAccountsVaultAccountIdUnhide,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_ACTIVATE: VaultAccountsVaultAccountIdAssetIdActivate,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_SET_CUSTOMER_REF_ID: VaultAccountsVaultAccountIdSetCustomerRefId,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_SET_AUTO_FUEL: VaultAccountsVaultAccountIdSetAutoFuel,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID: VaultAccountsVaultAccountIdAssetId,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_BALANCE: VaultAccountsVaultAccountIdAssetIdBalance,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_ADDRESSES: VaultAccountsVaultAccountIdAssetIdAddresses,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_MAX_SPENDABLE_AMOUNT: VaultAccountsVaultAccountIdAssetIdMaxSpendableAmount,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_ADDRESSES_ADDRESS_ID: VaultAccountsVaultAccountIdAssetIdAddressesAddressId,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_ADDRESSES_ADDRESS_ID_SET_CUSTOMER_REF_ID: VaultAccountsVaultAccountIdAssetIdAddressesAddressIdSetCustomerRefId,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_ADDRESSES_ADDRESS_ID_CREATE_LEGACY: VaultAccountsVaultAccountIdAssetIdAddressesAddressIdCreateLegacy,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_UNSPENT_INPUTS: VaultAccountsVaultAccountIdAssetIdUnspentInputs,
        PathValues.VAULT_PUBLIC_KEY_INFO_: VaultPublicKeyInfo,
        PathValues.VAULT_ACCOUNTS_VAULT_ACCOUNT_ID_ASSET_ID_CHANGE_ADDRESS_INDEX_PUBLIC_KEY_INFO: VaultAccountsVaultAccountIdAssetIdChangeAddressIndexPublicKeyInfo,
        PathValues.VAULT_ASSETS: VaultAssets,
        PathValues.VAULT_ASSETS_ASSET_ID: VaultAssetsAssetId,
        PathValues.EXCHANGE_ACCOUNTS: ExchangeAccounts,
        PathValues.EXCHANGE_ACCOUNTS_EXCHANGE_ACCOUNT_ID: ExchangeAccountsExchangeAccountId,
        PathValues.EXCHANGE_ACCOUNTS_EXCHANGE_ACCOUNT_ID_INTERNAL_TRANSFER: ExchangeAccountsExchangeAccountIdInternalTransfer,
        PathValues.EXCHANGE_ACCOUNTS_EXCHANGE_ACCOUNT_ID_CONVERT: ExchangeAccountsExchangeAccountIdConvert,
        PathValues.EXCHANGE_ACCOUNTS_EXCHANGE_ACCOUNT_ID_ASSET_ID: ExchangeAccountsExchangeAccountIdAssetId,
        PathValues.FIAT_ACCOUNTS: FiatAccounts,
        PathValues.FIAT_ACCOUNTS_ACCOUNT_ID: FiatAccountsAccountId,
        PathValues.FIAT_ACCOUNTS_ACCOUNT_ID_REDEEM_TO_LINKED_DDA: FiatAccountsAccountIdRedeemToLinkedDda,
        PathValues.FIAT_ACCOUNTS_ACCOUNT_ID_DEPOSIT_FROM_LINKED_DDA: FiatAccountsAccountIdDepositFromLinkedDda,
        PathValues.NETWORK_CONNECTIONS: NetworkConnections,
        PathValues.NETWORK_CONNECTIONS_CONNECTION_ID_SET_ROUTING_POLICY: NetworkConnectionsConnectionIdSetRoutingPolicy,
        PathValues.NETWORK_CONNECTIONS_CONNECTION_ID_IS_THIRD_PARTY_ROUTING_ASSET_TYPE: NetworkConnectionsConnectionIdIsThirdPartyRoutingAssetType,
        PathValues.NETWORK_CONNECTIONS_CONNECTION_ID: NetworkConnectionsConnectionId,
        PathValues.NETWORK_IDS: NetworkIds,
        PathValues.NETWORK_IDS_NETWORK_ID: NetworkIdsNetworkId,
        PathValues.NETWORK_IDS_NETWORK_ID_SET_ROUTING_POLICY: NetworkIdsNetworkIdSetRoutingPolicy,
        PathValues.NETWORK_IDS_NETWORK_ID_SET_DISCOVERABILITY: NetworkIdsNetworkIdSetDiscoverability,
        PathValues.NETWORK_IDS_NETWORK_ID_SET_NAME: NetworkIdsNetworkIdSetName,
        PathValues.INTERNAL_WALLETS: InternalWallets,
        PathValues.INTERNAL_WALLETS_WALLET_ID: InternalWalletsWalletId,
        PathValues.INTERNAL_WALLETS_WALLET_ID_SET_CUSTOMER_REF_ID: InternalWalletsWalletIdSetCustomerRefId,
        PathValues.INTERNAL_WALLETS_WALLET_ID_ASSET_ID: InternalWalletsWalletIdAssetId,
        PathValues.EXTERNAL_WALLETS: ExternalWallets,
        PathValues.EXTERNAL_WALLETS_WALLET_ID: ExternalWalletsWalletId,
        PathValues.EXTERNAL_WALLETS_WALLET_ID_SET_CUSTOMER_REF_ID: ExternalWalletsWalletIdSetCustomerRefId,
        PathValues.EXTERNAL_WALLETS_WALLET_ID_ASSET_ID: ExternalWalletsWalletIdAssetId,
        PathValues.CONTRACTS: Contracts,
        PathValues.CONTRACTS_CONTRACT_ID: ContractsContractId,
        PathValues.CONTRACTS_CONTRACT_ID_ASSET_ID: ContractsContractIdAssetId,
        PathValues.SUPPORTED_ASSETS: SupportedAssets,
        PathValues.TRANSACTIONS: Transactions,
        PathValues.TRANSACTIONS_ESTIMATE_FEE: TransactionsEstimateFee,
        PathValues.TRANSACTIONS_TX_ID: TransactionsTxId,
        PathValues.TRANSACTIONS_EXTERNAL_TX_ID_EXTERNAL_TX_ID_: TransactionsExternalTxIdExternalTxId,
        PathValues.TRANSACTIONS_TX_ID_SET_CONFIRMATION_THRESHOLD: TransactionsTxIdSetConfirmationThreshold,
        PathValues.TRANSACTIONS_TX_ID_DROP: TransactionsTxIdDrop,
        PathValues.TRANSACTIONS_TX_ID_CANCEL: TransactionsTxIdCancel,
        PathValues.TRANSACTIONS_TX_ID_FREEZE: TransactionsTxIdFreeze,
        PathValues.TRANSACTIONS_TX_ID_UNFREEZE: TransactionsTxIdUnfreeze,
        PathValues.TRANSACTIONS_VALIDATE_ADDRESS_ASSET_ID_ADDRESS: TransactionsValidateAddressAssetIdAddress,
        PathValues.TX_HASH_TX_HASH_SET_CONFIRMATION_THRESHOLD: TxHashTxHashSetConfirmationThreshold,
        PathValues.ESTIMATE_NETWORK_FEE: EstimateNetworkFee,
        PathValues.PAYMENTS_XBSETTLEMENTS_CONFIGS: PaymentsXbSettlementsConfigs,
        PathValues.PAYMENTS_XBSETTLEMENTS_CONFIGS_CONFIG_ID: PaymentsXbSettlementsConfigsConfigId,
        PathValues.PAYMENTS_XBSETTLEMENTS_FLOWS: PaymentsXbSettlementsFlows,
        PathValues.PAYMENTS_XBSETTLEMENTS_FLOWS_FLOW_ID: PaymentsXbSettlementsFlowsFlowId,
        PathValues.PAYMENTS_XBSETTLEMENTS_FLOWS_FLOW_ID_ACTIONS_EXECUTE: PaymentsXbSettlementsFlowsFlowIdActionsExecute,
        PathValues.PAYMENTS_PAYOUT: PaymentsPayout,
        PathValues.PAYMENTS_PAYOUT_PAYOUT_ID_ACTIONS_EXECUTE: PaymentsPayoutPayoutIdActionsExecute,
        PathValues.PAYMENTS_PAYOUT_PAYOUT_ID: PaymentsPayoutPayoutId,
        PathValues.GAS_STATION: GasStation,
        PathValues.GAS_STATION_ASSET_ID: GasStationAssetId,
        PathValues.GAS_STATION_CONFIGURATION: GasStationConfiguration,
        PathValues.GAS_STATION_CONFIGURATION_ASSET_ID: GasStationConfigurationAssetId,
        PathValues.USERS: Users,
        PathValues.AUDITS: Audits,
        PathValues.OFF_EXCHANGE_ADD: OffExchangeAdd,
        PathValues.OFF_EXCHANGE_REMOVE: OffExchangeRemove,
        PathValues.OFF_EXCHANGE_SETTLEMENTS_TRADER: OffExchangeSettlementsTrader,
        PathValues.OFF_EXCHANGE_SETTLEMENTS_TRANSACTIONS: OffExchangeSettlementsTransactions,
        PathValues.OFF_EXCHANGE_COLLATERAL_ACCOUNTS_MAIN_EXCHANGE_ACCOUNT_ID: OffExchangeCollateralAccountsMainExchangeAccountId,
        PathValues.WEBHOOKS_RESEND: WebhooksResend,
        PathValues.WEBHOOKS_RESEND_TX_ID: WebhooksResendTxId,
        PathValues.NFTS_OWNERSHIP_TOKENS: NftsOwnershipTokens,
        PathValues.NFTS_OWNERSHIP_COLLECTIONS: NftsOwnershipCollections,
        PathValues.NFTS_TOKENS_ID: NftsTokensId,
        PathValues.NFTS_TOKENS: NftsTokens,
        PathValues.NFTS_OWNERSHIP_TOKENS_ID_STATUS: NftsOwnershipTokensIdStatus,
        PathValues.CONNECTIONS: Connections,
        PathValues.CONNECTIONS_WC: ConnectionsWc,
        PathValues.CONNECTIONS_WC_ID: ConnectionsWcId,
        PathValues.SCREENING_TRAVEL_RULE_TRANSACTION_VALIDATE: ScreeningTravelRuleTransactionValidate,
        PathValues.SCREENING_TRAVEL_RULE_TRANSACTION_VALIDATE_FULL: ScreeningTravelRuleTransactionValidateFull,
        PathValues.SCREENING_TRAVEL_RULE_VASP_DID: ScreeningTravelRuleVaspDid,
        PathValues.SCREENING_TRAVEL_RULE_VASP: ScreeningTravelRuleVasp,
        PathValues.SCREEENING_TRAVEL_RULE_VASP_UPDATE: ScreeeningTravelRuleVaspUpdate,
        PathValues.TAP_ACTIVE_POLICY: TapActivePolicy,
        PathValues.TAP_DRAFT: TapDraft,
        PathValues.TAP_PUBLISH: TapPublish,
    }
)
