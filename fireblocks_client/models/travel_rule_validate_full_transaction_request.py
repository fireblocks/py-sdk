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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks_client.models.travel_rule_ownership_proof import TravelRuleOwnershipProof
from fireblocks_client.models.travel_rule_pii_ivms import TravelRulePiiIVMS
from fireblocks_client.models.travel_rule_transaction_blockchain_info import TravelRuleTransactionBlockchainInfo
from typing import Optional, Set
from typing_extensions import Self

class TravelRuleValidateFullTransactionRequest(BaseModel):
    """
    TravelRuleValidateFullTransactionRequest
    """ # noqa: E501
    transaction_asset: Optional[StrictStr] = Field(default=None, description="The asset involved in the transaction", alias="transactionAsset")
    transaction_amount: Optional[StrictStr] = Field(default=None, description="The amount of the transaction", alias="transactionAmount")
    originator_did: Optional[StrictStr] = Field(default=None, description="The DID of the transaction originator", alias="originatorDid")
    beneficiary_did: Optional[StrictStr] = Field(default=None, description="The DID of the transaction beneficiary", alias="beneficiaryDid")
    originator_vas_pdid: Optional[StrictStr] = Field(default=None, description="The VASP ID of the transaction originator", alias="originatorVASPdid")
    beneficiary_vas_pdid: Optional[StrictStr] = Field(default=None, description="The VASP ID of the transaction beneficiary", alias="beneficiaryVASPdid")
    beneficiary_vas_pname: Optional[StrictStr] = Field(default=None, description="The name of the VASP acting as the beneficiary", alias="beneficiaryVASPname")
    transaction_blockchain_info: Optional[TravelRuleTransactionBlockchainInfo] = Field(default=None, description="Information about the blockchain transaction", alias="transactionBlockchainInfo")
    originator: TravelRulePiiIVMS = Field(description="Information about the originator of the transaction")
    beneficiary: TravelRulePiiIVMS = Field(description="Information about the beneficiary of the transaction")
    encrypted: Optional[StrictStr] = Field(default=None, description="Encrypted data related to the transaction")
    protocol: Optional[StrictStr] = Field(default=None, description="The protocol used to perform the travel rule")
    notification_email: Optional[StrictStr] = Field(default=None, description="The email address where a notification should be sent upon completion of the travel rule", alias="notificationEmail")
    skip_beneficiary_data_validation: Optional[StrictBool] = Field(default=None, description="Whether to skip validation of beneficiary data", alias="skipBeneficiaryDataValidation")
    travel_rule_behavior: Optional[StrictBool] = Field(default=None, description="Whether to check if the transaction is a TRAVEL_RULE in the beneficiary VASP's jurisdiction", alias="travelRuleBehavior")
    originator_proof: Optional[TravelRuleOwnershipProof] = Field(default=None, description="Ownership proof related to the originator of the transaction", alias="originatorProof")
    beneficiary_proof: Optional[TravelRuleOwnershipProof] = Field(default=None, description="Ownership proof related to the beneficiary of the transaction", alias="beneficiaryProof")
    pii: Optional[TravelRulePiiIVMS] = Field(default=None, description="Personal identifiable information related to the transaction")
    __properties: ClassVar[List[str]] = ["transactionAsset", "transactionAmount", "originatorDid", "beneficiaryDid", "originatorVASPdid", "beneficiaryVASPdid", "beneficiaryVASPname", "transactionBlockchainInfo", "originator", "beneficiary", "encrypted", "protocol", "notificationEmail", "skipBeneficiaryDataValidation", "travelRuleBehavior", "originatorProof", "beneficiaryProof", "pii"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TravelRuleValidateFullTransactionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of transaction_blockchain_info
        if self.transaction_blockchain_info:
            _dict['transactionBlockchainInfo'] = self.transaction_blockchain_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of originator
        if self.originator:
            _dict['originator'] = self.originator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of beneficiary
        if self.beneficiary:
            _dict['beneficiary'] = self.beneficiary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of originator_proof
        if self.originator_proof:
            _dict['originatorProof'] = self.originator_proof.to_dict()
        # override the default output from pydantic by calling `to_dict()` of beneficiary_proof
        if self.beneficiary_proof:
            _dict['beneficiaryProof'] = self.beneficiary_proof.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pii
        if self.pii:
            _dict['pii'] = self.pii.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TravelRuleValidateFullTransactionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transactionAsset": obj.get("transactionAsset"),
            "transactionAmount": obj.get("transactionAmount"),
            "originatorDid": obj.get("originatorDid"),
            "beneficiaryDid": obj.get("beneficiaryDid"),
            "originatorVASPdid": obj.get("originatorVASPdid"),
            "beneficiaryVASPdid": obj.get("beneficiaryVASPdid"),
            "beneficiaryVASPname": obj.get("beneficiaryVASPname"),
            "transactionBlockchainInfo": TravelRuleTransactionBlockchainInfo.from_dict(obj["transactionBlockchainInfo"]) if obj.get("transactionBlockchainInfo") is not None else None,
            "originator": TravelRulePiiIVMS.from_dict(obj["originator"]) if obj.get("originator") is not None else None,
            "beneficiary": TravelRulePiiIVMS.from_dict(obj["beneficiary"]) if obj.get("beneficiary") is not None else None,
            "encrypted": obj.get("encrypted"),
            "protocol": obj.get("protocol"),
            "notificationEmail": obj.get("notificationEmail"),
            "skipBeneficiaryDataValidation": obj.get("skipBeneficiaryDataValidation"),
            "travelRuleBehavior": obj.get("travelRuleBehavior"),
            "originatorProof": TravelRuleOwnershipProof.from_dict(obj["originatorProof"]) if obj.get("originatorProof") is not None else None,
            "beneficiaryProof": TravelRuleOwnershipProof.from_dict(obj["beneficiaryProof"]) if obj.get("beneficiaryProof") is not None else None,
            "pii": TravelRulePiiIVMS.from_dict(obj["pii"]) if obj.get("pii") is not None else None
        })
        return _obj


