# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RelatedRequestStatusType(str, Enum):
    """
    The status of the request
    """

    """
    allowed enum values
    """
    ERROR = 'error'
    CREATED = 'created'
    CANCELED = 'canceled'
    ACTIVATE_REQUESTED = 'activate_requested'
    APPROVE_INPROGRESS = 'approve_inprogress'
    APPROVE_INPROGRESS_SIGNED = 'approve_inprogress_signed'
    ACTIVATE_INPROGRESS = 'activate_inprogress'
    ACTIVATE_INPROGRESS_SIGNED = 'activate_inprogress_signed'
    ACTIVATE_INPROGRESS_CONFIRMED = 'activate_inprogress_confirmed'
    ACTIVATE_DONE = 'activate_done'
    DEACTIVATE_REQUESTED = 'deactivate_requested'
    DEACTIVATE_INPROGRESS = 'deactivate_inprogress'
    DEACTIVATE_INPROGRESS_SIGNED = 'deactivate_inprogress_signed'
    DEACTIVATE_INPROGRESS_CONFIRMED = 'deactivate_inprogress_confirmed'
    DEACTIVATE_DONE = 'deactivate_done'
    WITHDRAW_INPROGRESS = 'withdraw_inprogress'
    WITHDRAW_REQUESTED = 'withdraw_requested'
    WITHDRAW_INPROGRESS_CONFIRMED = 'withdraw_inprogress_confirmed'
    WITHDRAW_DONE = 'withdraw_done'
    CLAIM_REWARDS_REQUESTED = 'claim_rewards_requested'
    CLAIM_REWARDS_INPROGRESS = 'claim_rewards_inprogress'
    CLAIM_REWARDS_DONE = 'claim_rewards_done'
    PENDING = 'pending'
    PENDING_QUEUED = 'pending_queued'
    ACTIVE_OFFLINE = 'active_offline'
    ACTIVE_ONLINE = 'active_online'
    EXITING_ONLINE = 'exiting_online'
    EXITED = 'exited'
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    ACTIVATING = 'activating'
    DEACTIVATING = 'deactivating'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RelatedRequestStatusType from a JSON string"""
        return cls(json.loads(json_str))


