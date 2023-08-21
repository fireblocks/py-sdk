import typing_extensions

from fireblocks_client.apis.tags import TagValues
from fireblocks_client.apis.tags.audit_logs_api import AuditLogsApi
from fireblocks_client.apis.tags.blockchains_assets_api import BlockchainsAssetsApi
from fireblocks_client.apis.tags.contracts_api import ContractsApi
from fireblocks_client.apis.tags.exchange_accounts_api import ExchangeAccountsApi
from fireblocks_client.apis.tags.external_wallets_api import ExternalWalletsApi
from fireblocks_client.apis.tags.fiat_accounts_api import FiatAccountsApi
from fireblocks_client.apis.tags.gas_stations_api import GasStationsApi
from fireblocks_client.apis.tags.internal_wallets_api import InternalWalletsApi
from fireblocks_client.apis.tags.nfts_api import NFTsApi
from fireblocks_client.apis.tags.network_connections_api import NetworkConnectionsApi
from fireblocks_client.apis.tags.ota_beta_api import OTABetaApi
from fireblocks_client.apis.tags.off_exchanges_api import OffExchangesApi
from fireblocks_client.apis.tags.payments_payout_api import PaymentsPayoutApi
from fireblocks_client.apis.tags.payments_cross_border_settlement_api import PaymentsCrossBorderSettlementApi
from fireblocks_client.apis.tags.policy_editor_beta_api import PolicyEditorBetaApi
from fireblocks_client.apis.tags.transactions_api import TransactionsApi
from fireblocks_client.apis.tags.travel_rule_beta_api import TravelRuleBetaApi
from fireblocks_client.apis.tags.users_api import UsersApi
from fireblocks_client.apis.tags.users_groups_beta_api import UsersGroupsBetaApi
from fireblocks_client.apis.tags.vaults_api import VaultsApi
from fireblocks_client.apis.tags.web3_connections_api import Web3ConnectionsApi
from fireblocks_client.apis.tags.webhooks_api import WebhooksApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUDIT_LOGS: AuditLogsApi,
        TagValues.BLOCKCHAINS__ASSETS: BlockchainsAssetsApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.EXCHANGE_ACCOUNTS: ExchangeAccountsApi,
        TagValues.EXTERNAL_WALLETS: ExternalWalletsApi,
        TagValues.FIAT_ACCOUNTS: FiatAccountsApi,
        TagValues.GAS_STATIONS: GasStationsApi,
        TagValues.INTERNAL_WALLETS: InternalWalletsApi,
        TagValues.NFTS: NFTsApi,
        TagValues.NETWORK_CONNECTIONS: NetworkConnectionsApi,
        TagValues.OTA_BETA: OTABetaApi,
        TagValues.OFF_EXCHANGES: OffExchangesApi,
        TagValues.PAYMENTS__PAYOUT: PaymentsPayoutApi,
        TagValues.PAYMENTS__CROSSBORDER_SETTLEMENT: PaymentsCrossBorderSettlementApi,
        TagValues.POLICY_EDITOR_BETA: PolicyEditorBetaApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.TRAVEL_RULE_BETA: TravelRuleBetaApi,
        TagValues.USERS: UsersApi,
        TagValues.USERS_GROUPS_BETA: UsersGroupsBetaApi,
        TagValues.VAULTS: VaultsApi,
        TagValues.WEB3_CONNECTIONS: Web3ConnectionsApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUDIT_LOGS: AuditLogsApi,
        TagValues.BLOCKCHAINS__ASSETS: BlockchainsAssetsApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.EXCHANGE_ACCOUNTS: ExchangeAccountsApi,
        TagValues.EXTERNAL_WALLETS: ExternalWalletsApi,
        TagValues.FIAT_ACCOUNTS: FiatAccountsApi,
        TagValues.GAS_STATIONS: GasStationsApi,
        TagValues.INTERNAL_WALLETS: InternalWalletsApi,
        TagValues.NFTS: NFTsApi,
        TagValues.NETWORK_CONNECTIONS: NetworkConnectionsApi,
        TagValues.OTA_BETA: OTABetaApi,
        TagValues.OFF_EXCHANGES: OffExchangesApi,
        TagValues.PAYMENTS__PAYOUT: PaymentsPayoutApi,
        TagValues.PAYMENTS__CROSSBORDER_SETTLEMENT: PaymentsCrossBorderSettlementApi,
        TagValues.POLICY_EDITOR_BETA: PolicyEditorBetaApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.TRAVEL_RULE_BETA: TravelRuleBetaApi,
        TagValues.USERS: UsersApi,
        TagValues.USERS_GROUPS_BETA: UsersGroupsBetaApi,
        TagValues.VAULTS: VaultsApi,
        TagValues.WEB3_CONNECTIONS: Web3ConnectionsApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)
