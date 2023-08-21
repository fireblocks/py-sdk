# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from fireblocks_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    AUDIT_LOGS = "Audit Logs"
    BLOCKCHAINS__ASSETS = "Blockchains &amp; assets"
    CONTRACTS = "Contracts"
    EXCHANGE_ACCOUNTS = "Exchange accounts"
    EXTERNAL_WALLETS = "External wallets"
    FIAT_ACCOUNTS = "Fiat accounts"
    GAS_STATIONS = "Gas stations"
    INTERNAL_WALLETS = "Internal wallets"
    NFTS = "NFTs"
    NETWORK_CONNECTIONS = "Network connections"
    OTA_BETA = "OTA (Beta)"
    OFF_EXCHANGES = "Off exchanges"
    PAYMENTS__PAYOUT = "Payments - Payout"
    PAYMENTS__CROSSBORDER_SETTLEMENT = "Payments - cross-border settlement"
    POLICY_EDITOR_BETA = "Policy Editor (Beta)"
    TRANSACTIONS = "Transactions"
    TRAVEL_RULE_BETA = "Travel Rule (Beta)"
    USERS = "Users"
    USERS_GROUPS_BETA = "Users groups (Beta)"
    VAULTS = "Vaults"
    WEB3_CONNECTIONS = "Web3 connections"
    WEBHOOKS = "Webhooks"
