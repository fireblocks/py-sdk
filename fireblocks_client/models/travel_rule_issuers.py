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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List
from fireblocks_client.models.travel_rule_issuer import TravelRuleIssuer
from typing import Optional, Set
from typing_extensions import Self

class TravelRuleIssuers(BaseModel):
    """
    TravelRuleIssuers
    """ # noqa: E501
    year_founded: TravelRuleIssuer = Field(alias="yearFounded")
    is_regulated: TravelRuleIssuer = Field(alias="isRegulated")
    regulatory_authorities: TravelRuleIssuer = Field(alias="regulatoryAuthorities")
    name: TravelRuleIssuer
    logo: TravelRuleIssuer
    website: TravelRuleIssuer
    legal_name: TravelRuleIssuer = Field(alias="legalName")
    legal_structure: TravelRuleIssuer = Field(alias="legalStructure")
    incorporation_country: TravelRuleIssuer = Field(alias="incorporationCountry")
    business_number: TravelRuleIssuer = Field(alias="businessNumber")
    address_line1: TravelRuleIssuer = Field(alias="addressLine1")
    city: TravelRuleIssuer
    country: TravelRuleIssuer
    description: TravelRuleIssuer
    __properties: ClassVar[List[str]] = ["yearFounded", "isRegulated", "regulatoryAuthorities", "name", "logo", "website", "legalName", "legalStructure", "incorporationCountry", "businessNumber", "addressLine1", "city", "country", "description"]

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
        """Create an instance of TravelRuleIssuers from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of year_founded
        if self.year_founded:
            _dict['yearFounded'] = self.year_founded.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_regulated
        if self.is_regulated:
            _dict['isRegulated'] = self.is_regulated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of regulatory_authorities
        if self.regulatory_authorities:
            _dict['regulatoryAuthorities'] = self.regulatory_authorities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of website
        if self.website:
            _dict['website'] = self.website.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legal_name
        if self.legal_name:
            _dict['legalName'] = self.legal_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legal_structure
        if self.legal_structure:
            _dict['legalStructure'] = self.legal_structure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of incorporation_country
        if self.incorporation_country:
            _dict['incorporationCountry'] = self.incorporation_country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_number
        if self.business_number:
            _dict['businessNumber'] = self.business_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address_line1
        if self.address_line1:
            _dict['addressLine1'] = self.address_line1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of city
        if self.city:
            _dict['city'] = self.city.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict['country'] = self.country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TravelRuleIssuers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "yearFounded": TravelRuleIssuer.from_dict(obj["yearFounded"]) if obj.get("yearFounded") is not None else None,
            "isRegulated": TravelRuleIssuer.from_dict(obj["isRegulated"]) if obj.get("isRegulated") is not None else None,
            "regulatoryAuthorities": TravelRuleIssuer.from_dict(obj["regulatoryAuthorities"]) if obj.get("regulatoryAuthorities") is not None else None,
            "name": TravelRuleIssuer.from_dict(obj["name"]) if obj.get("name") is not None else None,
            "logo": TravelRuleIssuer.from_dict(obj["logo"]) if obj.get("logo") is not None else None,
            "website": TravelRuleIssuer.from_dict(obj["website"]) if obj.get("website") is not None else None,
            "legalName": TravelRuleIssuer.from_dict(obj["legalName"]) if obj.get("legalName") is not None else None,
            "legalStructure": TravelRuleIssuer.from_dict(obj["legalStructure"]) if obj.get("legalStructure") is not None else None,
            "incorporationCountry": TravelRuleIssuer.from_dict(obj["incorporationCountry"]) if obj.get("incorporationCountry") is not None else None,
            "businessNumber": TravelRuleIssuer.from_dict(obj["businessNumber"]) if obj.get("businessNumber") is not None else None,
            "addressLine1": TravelRuleIssuer.from_dict(obj["addressLine1"]) if obj.get("addressLine1") is not None else None,
            "city": TravelRuleIssuer.from_dict(obj["city"]) if obj.get("city") is not None else None,
            "country": TravelRuleIssuer.from_dict(obj["country"]) if obj.get("country") is not None else None,
            "description": TravelRuleIssuer.from_dict(obj["description"]) if obj.get("description") is not None else None
        })
        return _obj


