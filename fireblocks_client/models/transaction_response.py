# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictStr, conlist, validator
from fireblocks_client.models.aml_screening_result import AmlScreeningResult
from fireblocks_client.models.amount_info import AmountInfo
from fireblocks_client.models.authorization_info import AuthorizationInfo
from fireblocks_client.models.block_info import BlockInfo
from fireblocks_client.models.destination_transfer_peer_path_response import DestinationTransferPeerPathResponse
from fireblocks_client.models.fee_info import FeeInfo
from fireblocks_client.models.get_transaction_operation import GetTransactionOperation
from fireblocks_client.models.network_record import NetworkRecord
from fireblocks_client.models.reward_info import RewardInfo
from fireblocks_client.models.signed_message import SignedMessage
from fireblocks_client.models.source_transfer_peer_path_response import SourceTransferPeerPathResponse
from fireblocks_client.models.system_message_info import SystemMessageInfo
from fireblocks_client.models.transaction_response_contract_call_decoded_data import TransactionResponseContractCallDecodedData
from fireblocks_client.models.transaction_response_destination import TransactionResponseDestination

class TransactionResponse(BaseModel):
    """
    TransactionResponse
    """
    id: Optional[StrictStr] = Field(None, description="ID of the transaction.")
    external_tx_id: Optional[StrictStr] = Field(None, alias="externalTxId", description="Unique transaction ID provided by the user. Fireblocks highly recommends setting an `externalTxId` for every transaction created, to avoid submitting the same transaction twice.")
    status: Optional[StrictStr] = Field(None, description="The primary status of the transaction. For details, see [Primary transaction statuses](https://developers.fireblocks.com/reference/primary-transaction-statuses).")
    sub_status: Optional[StrictStr] = Field(None, alias="subStatus", description="See [Transaction substatuses](https://developers.fireblocks.com/reference/transaction-substatuses) for the list of transaction sub statuses.")
    tx_hash: Optional[StrictStr] = Field(None, alias="txHash", description="The hash of the transaction on the blockchain.  * This parameter exists if at least one of the following conditions is met:       1. The transaction’s source type is `UNKNOWN`, `WHITELISTED_ADDRESS`, `NETWORK_CONNECTION`, `ONE_TIME_ADDRESS`, `FIAT_ACCOUNT` or `GAS_STATION`.       2. The transaction’s source type is `VAULT` and the status is either: `CONFIRMING`, `COMPLETED`, or was in any of these statuses prior to changing to `FAILED` or `REJECTED`. In some instances, transactions in status `BROADCASTING` will include the txHash as well.       3. The transaction’s source type is `EXCHANGE_ACCOUNT` and the transaction’s destination type is `VAULT`, and the status is either: `CONFIRMING`, `COMPLETED`, or was in any of these status prior to changing to `FAILED`.   * In addition, the following conditions must be met:      1. The asset is a crypto asset (not fiat).      2. The transaction operation is not RAW or `TYPED_MESSAGE`.")
    operation: Optional[GetTransactionOperation] = None
    note: Optional[StrictStr] = Field(None, description="Custom note, not sent to the blockchain, that describes the transaction at your Fireblocks workspace.")
    asset_id: Optional[StrictStr] = Field(None, alias="assetId", description="The ID of the asset to transfer, for `TRANSFER`, `MINT`, `BURN`, `ENABLE_ASSET`,`STAKE` ,`UNSTAKE` or `WITHDRAW` operations. [See the list of supported assets and their IDs on Fireblocks.](https://developers.fireblocks.com/reference/get_supported-assets)")
    source: Optional[SourceTransferPeerPathResponse] = None
    source_address: Optional[StrictStr] = Field(None, alias="sourceAddress", description="For account based assets only, the source address of the transaction. **Note:** If the status is `CONFIRMING`, `COMPLETED`, or has been `CONFIRMING`; then moved forward to `FAILED` or `REJECTED`, then this parameter will contain the source address. In any other case, this parameter will be empty.")
    tag: Optional[StrictStr] = Field(None, description="Source address tag for XRP, used as memo for EOS/XLM, or Bank Transfer Description for the fiat provider BLINC (by BCB Group).")
    destination: Optional[DestinationTransferPeerPathResponse] = None
    destinations: Optional[conlist(TransactionResponseDestination)] = Field(None, description="The transaction’s destinations. **Note:** In case the transaction is sent to a single destination, the `destination` parameter is used instead of this.")
    destination_address: Optional[StrictStr] = Field(None, alias="destinationAddress", description="Address where the asset were transferred. Notes:   - For [Multi destination transactions](https://support.fireblocks.io/hc/en-us/articles/360018447980-Multi-destination-transactions), this parameter will be empty. In this case, you should refer to the destinations field.   - If the status is `CONFIRMING`, `COMPLETED`, or has been `CONFIRMING`; then moved forward to `FAILED` or `REJECTED`, then this parameter will contain the destination address. In any other case, this parameter will be empty.")
    destination_address_description: Optional[StrictStr] = Field(None, alias="destinationAddressDescription", description="Description of the address.")
    destination_tag: Optional[StrictStr] = Field(None, alias="destinationTag", description="Destination address tag for XRP, used as memo for EOS/XLM, or Bank Transfer Description for the fiat provider BLINC (by BCB Group).")
    contract_call_decoded_data: Optional[TransactionResponseContractCallDecodedData] = Field(None, alias="contractCallDecodedData")
    amount_info: Optional[AmountInfo] = Field(None, alias="amountInfo")
    treat_as_gross_amount: Optional[StrictBool] = Field(None, alias="treatAsGrossAmount", description="For transactions initiated via this Fireblocks workspace, when set to `true`, the fee is deducted from the requested amount.")
    fee_info: Optional[FeeInfo] = Field(None, alias="feeInfo")
    fee_currency: Optional[StrictStr] = Field(None, alias="feeCurrency", description="The asset which was withdrawn to pay the transaction fee, for example ETH for EVM-based blockchains, BTC for Tether Omni.")
    network_records: Optional[conlist(NetworkRecord)] = Field(None, alias="networkRecords", description="In case a single transaction resulted with multiple transfers, for example a result of a contract call, then this parameter specifies each transfer that took place on the blockchain. In case of a single transfer transaction, this parameter is empty.")
    created_at: Optional[StrictFloat] = Field(None, alias="createdAt", description="The transaction’s creation date and time, in unix timestamp.")
    last_updated: Optional[StrictFloat] = Field(None, alias="lastUpdated", description="The transaction’s last update date and time, in unix timestamp.")
    created_by: Optional[StrictStr] = Field(None, alias="createdBy", description="User ID of the initiator of the transaction.")
    signed_by: Optional[conlist(StrictStr)] = Field(None, alias="signedBy", description="User ID’s of the signers of the transaction.")
    rejected_by: Optional[StrictStr] = Field(None, alias="rejectedBy", description="User ID of the user that rejected the transaction (in case it was rejected).")
    authorization_info: Optional[AuthorizationInfo] = Field(None, alias="authorizationInfo")
    exchange_tx_id: Optional[StrictStr] = Field(None, alias="exchangeTxId", description="If the transaction originated from an exchange, this is the ID of this transaction at the exchange.")
    customer_ref_id: Optional[StrictStr] = Field(None, alias="customerRefId", description="The ID for AML providers to associate the owner of funds with transactions.")
    aml_screening_result: Optional[AmlScreeningResult] = Field(None, alias="amlScreeningResult")
    extra_parameters: Optional[Dict[str, Any]] = Field(None, alias="extraParameters", description="Additional protocol / operation specific key-value parameters:  For UTXO-based blockchain input selection, add the key `inputsSelection` with the value set the [input selection structure.](https://developers.fireblocks.com/reference/transaction-objects#inputsselection) The inputs can be retrieved from the [Retrieve Unspent Inputs endpoint.](https://developers.fireblocks.com/reference/get_vault-accounts-vaultaccountid-assetid-unspent-inputs)  For `RAW` operations, add the key `rawMessageData` with the value set to the [raw message data structure.](https://developers.fireblocks.com/reference/raw-signing-objects#rawmessagedata)  For `CONTRACT_CALL` operations, add the key `contractCallData` with the value set to the Ethereum smart contract Application Binary Interface (ABI) payload. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions. ")
    signed_messages: Optional[SignedMessage] = Field(None, alias="signedMessages")
    num_of_confirmations: Optional[StrictFloat] = Field(None, alias="numOfConfirmations", description="The number of confirmations of the transaction. The number will increase until the transaction will be considered completed according to the confirmation policy.")
    block_info: Optional[BlockInfo] = Field(None, alias="blockInfo")
    index: Optional[StrictFloat] = Field(None, description="For UTXO based assets this is the vOut, for Ethereum based, this is the index of the event of the contract call.  **Note:** This field is not returned if a transaction uses the `destinations` object with more than one value.")
    reward_info: Optional[RewardInfo] = Field(None, alias="rewardInfo")
    system_messages: Optional[SystemMessageInfo] = Field(None, alias="systemMessages")
    address_type: Optional[StrictStr] = Field(None, alias="addressType")
    requested_amount: Optional[StrictFloat] = Field(None, alias="requestedAmount", description="The amount requested by the user. Deprecated - please use the `amountInfo` field for accuracy.")
    amount: Optional[StrictFloat] = Field(None, description="If the transfer is a withdrawal from an exchange, the actual amount that was requested to be transferred. Otherwise, the requested amount. Deprecated - please use the `amountInfo` field for accuracy.")
    net_amount: Optional[StrictFloat] = Field(None, alias="netAmount", description="The net amount of the transaction, after fee deduction. Deprecated - please use the `amountInfo` field for accuracy.")
    amount_usd: Optional[StrictFloat] = Field(None, alias="amountUSD", description="The USD value of the requested amount. Deprecated - please use the `amountInfo` field for accuracy.")
    service_fee: Optional[StrictFloat] = Field(None, alias="serviceFee", description="The total fee deducted by the exchange from the actual requested amount (`serviceFee` = `amount` - `netAmount`). Deprecated - please use the `feeInfo` field for accuracy.")
    fee: Optional[StrictFloat] = Field(None, description="Deprecated - please use the `feeInfo` field for accuracy.")
    network_fee: Optional[StrictFloat] = Field(None, alias="networkFee", description="The fee paid to the network. Deprecated - please use the `feeInfo` field for accuracy.")
    __properties = ["id", "externalTxId", "status", "subStatus", "txHash", "operation", "note", "assetId", "source", "sourceAddress", "tag", "destination", "destinations", "destinationAddress", "destinationAddressDescription", "destinationTag", "contractCallDecodedData", "amountInfo", "treatAsGrossAmount", "feeInfo", "feeCurrency", "networkRecords", "createdAt", "lastUpdated", "createdBy", "signedBy", "rejectedBy", "authorizationInfo", "exchangeTxId", "customerRefId", "amlScreeningResult", "extraParameters", "signedMessages", "numOfConfirmations", "blockInfo", "index", "rewardInfo", "systemMessages", "addressType", "requestedAmount", "amount", "netAmount", "amountUSD", "serviceFee", "fee", "networkFee"]

    @validator('address_type')
    def address_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('WHITELISTED', 'ONE_TIME'):
            raise ValueError("must be one of enum values ('WHITELISTED', 'ONE_TIME')")
        return v

    class Config:
        populate_by_name = True
        validate_assignment = True
        arbitrary_types_allowed = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TransactionResponse:
        """Create an instance of TransactionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in destinations (list)
        _items = []
        if self.destinations:
            for _item in self.destinations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['destinations'] = _items
        # override the default output from pydantic by calling `to_dict()` of contract_call_decoded_data
        if self.contract_call_decoded_data:
            _dict['contractCallDecodedData'] = self.contract_call_decoded_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount_info
        if self.amount_info:
            _dict['amountInfo'] = self.amount_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fee_info
        if self.fee_info:
            _dict['feeInfo'] = self.fee_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in network_records (list)
        _items = []
        if self.network_records:
            for _item in self.network_records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['networkRecords'] = _items
        # override the default output from pydantic by calling `to_dict()` of authorization_info
        if self.authorization_info:
            _dict['authorizationInfo'] = self.authorization_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aml_screening_result
        if self.aml_screening_result:
            _dict['amlScreeningResult'] = self.aml_screening_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of signed_messages
        if self.signed_messages:
            _dict['signedMessages'] = self.signed_messages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of block_info
        if self.block_info:
            _dict['blockInfo'] = self.block_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reward_info
        if self.reward_info:
            _dict['rewardInfo'] = self.reward_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system_messages
        if self.system_messages:
            _dict['systemMessages'] = self.system_messages.to_dict()
        # set to None if amount_usd (nullable) is None
        # and __fields_set__ contains the field
        if self.amount_usd is None and "amount_usd" in self.__fields_set__:
            _dict['amountUSD'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionResponse:
        """Create an instance of TransactionResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TransactionResponse.parse_obj(obj)

        _obj = TransactionResponse.parse_obj({
            "id": obj.get("id"),
            "external_tx_id": obj.get("externalTxId"),
            "status": obj.get("status"),
            "sub_status": obj.get("subStatus"),
            "tx_hash": obj.get("txHash"),
            "operation": obj.get("operation"),
            "note": obj.get("note"),
            "asset_id": obj.get("assetId"),
            "source": SourceTransferPeerPathResponse.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "source_address": obj.get("sourceAddress"),
            "tag": obj.get("tag"),
            "destination": DestinationTransferPeerPathResponse.from_dict(obj.get("destination")) if obj.get("destination") is not None else None,
            "destinations": [TransactionResponseDestination.from_dict(_item) for _item in obj.get("destinations")] if obj.get("destinations") is not None else None,
            "destination_address": obj.get("destinationAddress"),
            "destination_address_description": obj.get("destinationAddressDescription"),
            "destination_tag": obj.get("destinationTag"),
            "contract_call_decoded_data": TransactionResponseContractCallDecodedData.from_dict(obj.get("contractCallDecodedData")) if obj.get("contractCallDecodedData") is not None else None,
            "amount_info": AmountInfo.from_dict(obj.get("amountInfo")) if obj.get("amountInfo") is not None else None,
            "treat_as_gross_amount": obj.get("treatAsGrossAmount"),
            "fee_info": FeeInfo.from_dict(obj.get("feeInfo")) if obj.get("feeInfo") is not None else None,
            "fee_currency": obj.get("feeCurrency"),
            "network_records": [NetworkRecord.from_dict(_item) for _item in obj.get("networkRecords")] if obj.get("networkRecords") is not None else None,
            "created_at": obj.get("createdAt"),
            "last_updated": obj.get("lastUpdated"),
            "created_by": obj.get("createdBy"),
            "signed_by": obj.get("signedBy"),
            "rejected_by": obj.get("rejectedBy"),
            "authorization_info": AuthorizationInfo.from_dict(obj.get("authorizationInfo")) if obj.get("authorizationInfo") is not None else None,
            "exchange_tx_id": obj.get("exchangeTxId"),
            "customer_ref_id": obj.get("customerRefId"),
            "aml_screening_result": AmlScreeningResult.from_dict(obj.get("amlScreeningResult")) if obj.get("amlScreeningResult") is not None else None,
            "extra_parameters": obj.get("extraParameters"),
            "signed_messages": SignedMessage.from_dict(obj.get("signedMessages")) if obj.get("signedMessages") is not None else None,
            "num_of_confirmations": obj.get("numOfConfirmations"),
            "block_info": BlockInfo.from_dict(obj.get("blockInfo")) if obj.get("blockInfo") is not None else None,
            "index": obj.get("index"),
            "reward_info": RewardInfo.from_dict(obj.get("rewardInfo")) if obj.get("rewardInfo") is not None else None,
            "system_messages": SystemMessageInfo.from_dict(obj.get("systemMessages")) if obj.get("systemMessages") is not None else None,
            "address_type": obj.get("addressType"),
            "requested_amount": obj.get("requestedAmount"),
            "amount": obj.get("amount"),
            "net_amount": obj.get("netAmount"),
            "amount_usd": obj.get("amountUSD"),
            "service_fee": obj.get("serviceFee"),
            "fee": obj.get("fee"),
            "network_fee": obj.get("networkFee")
        })
        return _obj

