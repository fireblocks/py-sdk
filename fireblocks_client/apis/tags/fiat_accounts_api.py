# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by: https://openapi-generator.tech
"""

from fireblocks_client.paths.fiat_accounts_account_id_deposit_from_linked_dda.post import DepositFundsFromLinkedDda
from fireblocks_client.paths.fiat_accounts_account_id.get import GetFiatAccountById
from fireblocks_client.paths.fiat_accounts.get import GetFiatAccounts
from fireblocks_client.paths.fiat_accounts_account_id_redeem_to_linked_dda.post import RedeemFundsToLinkedDda


class FiatAccountsApi(
    DepositFundsFromLinkedDda,
    GetFiatAccountById,
    GetFiatAccounts,
    RedeemFundsToLinkedDda,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
