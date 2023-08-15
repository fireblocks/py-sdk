# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from fireblocks_client import schemas  # noqa: F401


class TravelRuleVASP(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "country",
            "travelRule_TRISA",
            "isNotifiable",
            "travelRule_TRP",
            "city",
            "documents",
            "isRegulated",
            "travelRule_EMAIL",
            "description",
            "identificationType",
            "identificationCountry",
            "travelRule_SYGNA",
            "lastReceivedDate",
            "legalName",
            "createdAt",
            "number",
            "legalStructure",
            "street",
            "travelRule_SHYFT",
            "regulatoryAuthorities",
            "addressLine1",
            "logo",
            "addressLine2",
            "state",
            "jurisdictions",
            "travelRule_TRLIGHT",
            "updatedAt",
            "hasAdmin",
            "website",
            "updatedBy",
            "verificationStatus",
            "emailDomains",
            "businessNumber",
            "issuers",
            "yearFounded",
            "travelRule_OPENVASP",
            "travelRule_USTRAVELRULEWG",
            "unit",
            "otherNames",
            "certificates",
            "lastSentDate",
            "createdBy",
            "name",
            "postCode",
            "did",
            "incorporationCountry",
        }
        
        class properties:
            did = schemas.StrSchema
            name = schemas.StrSchema
            verificationStatus = schemas.StrSchema
            addressLine1 = schemas.StrSchema
            addressLine2 = schemas.StrSchema
            city = schemas.StrSchema
            country = schemas.StrSchema
            emailDomains = schemas.StrSchema
            website = schemas.StrSchema
            logo = schemas.StrSchema
            legalStructure = schemas.StrSchema
            legalName = schemas.StrSchema
            yearFounded = schemas.StrSchema
            incorporationCountry = schemas.StrSchema
            isRegulated = schemas.StrSchema
            otherNames = schemas.StrSchema
            identificationType = schemas.StrSchema
            identificationCountry = schemas.StrSchema
            businessNumber = schemas.StrSchema
            regulatoryAuthorities = schemas.StrSchema
            jurisdictions = schemas.StrSchema
            street = schemas.StrSchema
            number = schemas.StrSchema
            unit = schemas.StrSchema
            postCode = schemas.StrSchema
            state = schemas.StrSchema
            certificates = schemas.StrSchema
            description = schemas.StrSchema
            travelRule_OPENVASP = schemas.StrSchema
            travelRule_SYGNA = schemas.StrSchema
            travelRule_TRISA = schemas.StrSchema
            travelRule_TRLIGHT = schemas.StrSchema
            travelRule_EMAIL = schemas.StrSchema
            travelRule_TRP = schemas.StrSchema
            travelRule_SHYFT = schemas.StrSchema
            travelRule_USTRAVELRULEWG = schemas.StrSchema
            createdAt = schemas.StrSchema
            createdBy = schemas.StrSchema
            updatedAt = schemas.StrSchema
            updatedBy = schemas.StrSchema
            lastSentDate = schemas.StrSchema
            lastReceivedDate = schemas.StrSchema
            documents = schemas.StrSchema
            hasAdmin = schemas.BoolSchema
            isNotifiable = schemas.BoolSchema
        
            @staticmethod
            def issuers() -> typing.Type['TravelRuleIssuers']:
                return TravelRuleIssuers
            __annotations__ = {
                "did": did,
                "name": name,
                "verificationStatus": verificationStatus,
                "addressLine1": addressLine1,
                "addressLine2": addressLine2,
                "city": city,
                "country": country,
                "emailDomains": emailDomains,
                "website": website,
                "logo": logo,
                "legalStructure": legalStructure,
                "legalName": legalName,
                "yearFounded": yearFounded,
                "incorporationCountry": incorporationCountry,
                "isRegulated": isRegulated,
                "otherNames": otherNames,
                "identificationType": identificationType,
                "identificationCountry": identificationCountry,
                "businessNumber": businessNumber,
                "regulatoryAuthorities": regulatoryAuthorities,
                "jurisdictions": jurisdictions,
                "street": street,
                "number": number,
                "unit": unit,
                "postCode": postCode,
                "state": state,
                "certificates": certificates,
                "description": description,
                "travelRule_OPENVASP": travelRule_OPENVASP,
                "travelRule_SYGNA": travelRule_SYGNA,
                "travelRule_TRISA": travelRule_TRISA,
                "travelRule_TRLIGHT": travelRule_TRLIGHT,
                "travelRule_EMAIL": travelRule_EMAIL,
                "travelRule_TRP": travelRule_TRP,
                "travelRule_SHYFT": travelRule_SHYFT,
                "travelRule_USTRAVELRULEWG": travelRule_USTRAVELRULEWG,
                "createdAt": createdAt,
                "createdBy": createdBy,
                "updatedAt": updatedAt,
                "updatedBy": updatedBy,
                "lastSentDate": lastSentDate,
                "lastReceivedDate": lastReceivedDate,
                "documents": documents,
                "hasAdmin": hasAdmin,
                "isNotifiable": isNotifiable,
                "issuers": issuers,
            }
    
    country: MetaOapg.properties.country
    travelRule_TRISA: MetaOapg.properties.travelRule_TRISA
    isNotifiable: MetaOapg.properties.isNotifiable
    travelRule_TRP: MetaOapg.properties.travelRule_TRP
    city: MetaOapg.properties.city
    documents: MetaOapg.properties.documents
    isRegulated: MetaOapg.properties.isRegulated
    travelRule_EMAIL: MetaOapg.properties.travelRule_EMAIL
    description: MetaOapg.properties.description
    identificationType: MetaOapg.properties.identificationType
    identificationCountry: MetaOapg.properties.identificationCountry
    travelRule_SYGNA: MetaOapg.properties.travelRule_SYGNA
    lastReceivedDate: MetaOapg.properties.lastReceivedDate
    legalName: MetaOapg.properties.legalName
    createdAt: MetaOapg.properties.createdAt
    number: MetaOapg.properties.number
    legalStructure: MetaOapg.properties.legalStructure
    street: MetaOapg.properties.street
    travelRule_SHYFT: MetaOapg.properties.travelRule_SHYFT
    regulatoryAuthorities: MetaOapg.properties.regulatoryAuthorities
    addressLine1: MetaOapg.properties.addressLine1
    logo: MetaOapg.properties.logo
    addressLine2: MetaOapg.properties.addressLine2
    state: MetaOapg.properties.state
    jurisdictions: MetaOapg.properties.jurisdictions
    travelRule_TRLIGHT: MetaOapg.properties.travelRule_TRLIGHT
    updatedAt: MetaOapg.properties.updatedAt
    hasAdmin: MetaOapg.properties.hasAdmin
    website: MetaOapg.properties.website
    updatedBy: MetaOapg.properties.updatedBy
    verificationStatus: MetaOapg.properties.verificationStatus
    emailDomains: MetaOapg.properties.emailDomains
    businessNumber: MetaOapg.properties.businessNumber
    issuers: 'TravelRuleIssuers'
    yearFounded: MetaOapg.properties.yearFounded
    travelRule_OPENVASP: MetaOapg.properties.travelRule_OPENVASP
    travelRule_USTRAVELRULEWG: MetaOapg.properties.travelRule_USTRAVELRULEWG
    unit: MetaOapg.properties.unit
    otherNames: MetaOapg.properties.otherNames
    certificates: MetaOapg.properties.certificates
    lastSentDate: MetaOapg.properties.lastSentDate
    createdBy: MetaOapg.properties.createdBy
    name: MetaOapg.properties.name
    postCode: MetaOapg.properties.postCode
    did: MetaOapg.properties.did
    incorporationCountry: MetaOapg.properties.incorporationCountry
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["did"]) -> MetaOapg.properties.did: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verificationStatus"]) -> MetaOapg.properties.verificationStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressLine1"]) -> MetaOapg.properties.addressLine1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressLine2"]) -> MetaOapg.properties.addressLine2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailDomains"]) -> MetaOapg.properties.emailDomains: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalStructure"]) -> MetaOapg.properties.legalStructure: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalName"]) -> MetaOapg.properties.legalName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["yearFounded"]) -> MetaOapg.properties.yearFounded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["incorporationCountry"]) -> MetaOapg.properties.incorporationCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isRegulated"]) -> MetaOapg.properties.isRegulated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherNames"]) -> MetaOapg.properties.otherNames: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identificationType"]) -> MetaOapg.properties.identificationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identificationCountry"]) -> MetaOapg.properties.identificationCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["businessNumber"]) -> MetaOapg.properties.businessNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regulatoryAuthorities"]) -> MetaOapg.properties.regulatoryAuthorities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jurisdictions"]) -> MetaOapg.properties.jurisdictions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street"]) -> MetaOapg.properties.street: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postCode"]) -> MetaOapg.properties.postCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["certificates"]) -> MetaOapg.properties.certificates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["travelRule_OPENVASP"]) -> MetaOapg.properties.travelRule_OPENVASP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["travelRule_SYGNA"]) -> MetaOapg.properties.travelRule_SYGNA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["travelRule_TRISA"]) -> MetaOapg.properties.travelRule_TRISA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["travelRule_TRLIGHT"]) -> MetaOapg.properties.travelRule_TRLIGHT: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["travelRule_EMAIL"]) -> MetaOapg.properties.travelRule_EMAIL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["travelRule_TRP"]) -> MetaOapg.properties.travelRule_TRP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["travelRule_SHYFT"]) -> MetaOapg.properties.travelRule_SHYFT: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["travelRule_USTRAVELRULEWG"]) -> MetaOapg.properties.travelRule_USTRAVELRULEWG: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdBy"]) -> MetaOapg.properties.createdBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedBy"]) -> MetaOapg.properties.updatedBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastSentDate"]) -> MetaOapg.properties.lastSentDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastReceivedDate"]) -> MetaOapg.properties.lastReceivedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documents"]) -> MetaOapg.properties.documents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasAdmin"]) -> MetaOapg.properties.hasAdmin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isNotifiable"]) -> MetaOapg.properties.isNotifiable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuers"]) -> 'TravelRuleIssuers': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["did", "name", "verificationStatus", "addressLine1", "addressLine2", "city", "country", "emailDomains", "website", "logo", "legalStructure", "legalName", "yearFounded", "incorporationCountry", "isRegulated", "otherNames", "identificationType", "identificationCountry", "businessNumber", "regulatoryAuthorities", "jurisdictions", "street", "number", "unit", "postCode", "state", "certificates", "description", "travelRule_OPENVASP", "travelRule_SYGNA", "travelRule_TRISA", "travelRule_TRLIGHT", "travelRule_EMAIL", "travelRule_TRP", "travelRule_SHYFT", "travelRule_USTRAVELRULEWG", "createdAt", "createdBy", "updatedAt", "updatedBy", "lastSentDate", "lastReceivedDate", "documents", "hasAdmin", "isNotifiable", "issuers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["did"]) -> MetaOapg.properties.did: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verificationStatus"]) -> MetaOapg.properties.verificationStatus: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressLine1"]) -> MetaOapg.properties.addressLine1: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressLine2"]) -> MetaOapg.properties.addressLine2: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailDomains"]) -> MetaOapg.properties.emailDomains: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalStructure"]) -> MetaOapg.properties.legalStructure: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalName"]) -> MetaOapg.properties.legalName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["yearFounded"]) -> MetaOapg.properties.yearFounded: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["incorporationCountry"]) -> MetaOapg.properties.incorporationCountry: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isRegulated"]) -> MetaOapg.properties.isRegulated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherNames"]) -> MetaOapg.properties.otherNames: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identificationType"]) -> MetaOapg.properties.identificationType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identificationCountry"]) -> MetaOapg.properties.identificationCountry: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["businessNumber"]) -> MetaOapg.properties.businessNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regulatoryAuthorities"]) -> MetaOapg.properties.regulatoryAuthorities: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jurisdictions"]) -> MetaOapg.properties.jurisdictions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street"]) -> MetaOapg.properties.street: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postCode"]) -> MetaOapg.properties.postCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["certificates"]) -> MetaOapg.properties.certificates: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["travelRule_OPENVASP"]) -> MetaOapg.properties.travelRule_OPENVASP: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["travelRule_SYGNA"]) -> MetaOapg.properties.travelRule_SYGNA: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["travelRule_TRISA"]) -> MetaOapg.properties.travelRule_TRISA: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["travelRule_TRLIGHT"]) -> MetaOapg.properties.travelRule_TRLIGHT: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["travelRule_EMAIL"]) -> MetaOapg.properties.travelRule_EMAIL: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["travelRule_TRP"]) -> MetaOapg.properties.travelRule_TRP: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["travelRule_SHYFT"]) -> MetaOapg.properties.travelRule_SHYFT: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["travelRule_USTRAVELRULEWG"]) -> MetaOapg.properties.travelRule_USTRAVELRULEWG: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdBy"]) -> MetaOapg.properties.createdBy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedBy"]) -> MetaOapg.properties.updatedBy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastSentDate"]) -> MetaOapg.properties.lastSentDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastReceivedDate"]) -> MetaOapg.properties.lastReceivedDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documents"]) -> MetaOapg.properties.documents: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasAdmin"]) -> MetaOapg.properties.hasAdmin: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isNotifiable"]) -> MetaOapg.properties.isNotifiable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuers"]) -> 'TravelRuleIssuers': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["did", "name", "verificationStatus", "addressLine1", "addressLine2", "city", "country", "emailDomains", "website", "logo", "legalStructure", "legalName", "yearFounded", "incorporationCountry", "isRegulated", "otherNames", "identificationType", "identificationCountry", "businessNumber", "regulatoryAuthorities", "jurisdictions", "street", "number", "unit", "postCode", "state", "certificates", "description", "travelRule_OPENVASP", "travelRule_SYGNA", "travelRule_TRISA", "travelRule_TRLIGHT", "travelRule_EMAIL", "travelRule_TRP", "travelRule_SHYFT", "travelRule_USTRAVELRULEWG", "createdAt", "createdBy", "updatedAt", "updatedBy", "lastSentDate", "lastReceivedDate", "documents", "hasAdmin", "isNotifiable", "issuers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, ],
        travelRule_TRISA: typing.Union[MetaOapg.properties.travelRule_TRISA, str, ],
        isNotifiable: typing.Union[MetaOapg.properties.isNotifiable, bool, ],
        travelRule_TRP: typing.Union[MetaOapg.properties.travelRule_TRP, str, ],
        city: typing.Union[MetaOapg.properties.city, str, ],
        documents: typing.Union[MetaOapg.properties.documents, str, ],
        isRegulated: typing.Union[MetaOapg.properties.isRegulated, str, ],
        travelRule_EMAIL: typing.Union[MetaOapg.properties.travelRule_EMAIL, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        identificationType: typing.Union[MetaOapg.properties.identificationType, str, ],
        identificationCountry: typing.Union[MetaOapg.properties.identificationCountry, str, ],
        travelRule_SYGNA: typing.Union[MetaOapg.properties.travelRule_SYGNA, str, ],
        lastReceivedDate: typing.Union[MetaOapg.properties.lastReceivedDate, str, ],
        legalName: typing.Union[MetaOapg.properties.legalName, str, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, ],
        number: typing.Union[MetaOapg.properties.number, str, ],
        legalStructure: typing.Union[MetaOapg.properties.legalStructure, str, ],
        street: typing.Union[MetaOapg.properties.street, str, ],
        travelRule_SHYFT: typing.Union[MetaOapg.properties.travelRule_SHYFT, str, ],
        regulatoryAuthorities: typing.Union[MetaOapg.properties.regulatoryAuthorities, str, ],
        addressLine1: typing.Union[MetaOapg.properties.addressLine1, str, ],
        logo: typing.Union[MetaOapg.properties.logo, str, ],
        addressLine2: typing.Union[MetaOapg.properties.addressLine2, str, ],
        state: typing.Union[MetaOapg.properties.state, str, ],
        jurisdictions: typing.Union[MetaOapg.properties.jurisdictions, str, ],
        travelRule_TRLIGHT: typing.Union[MetaOapg.properties.travelRule_TRLIGHT, str, ],
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, ],
        hasAdmin: typing.Union[MetaOapg.properties.hasAdmin, bool, ],
        website: typing.Union[MetaOapg.properties.website, str, ],
        updatedBy: typing.Union[MetaOapg.properties.updatedBy, str, ],
        verificationStatus: typing.Union[MetaOapg.properties.verificationStatus, str, ],
        emailDomains: typing.Union[MetaOapg.properties.emailDomains, str, ],
        businessNumber: typing.Union[MetaOapg.properties.businessNumber, str, ],
        issuers: 'TravelRuleIssuers',
        yearFounded: typing.Union[MetaOapg.properties.yearFounded, str, ],
        travelRule_OPENVASP: typing.Union[MetaOapg.properties.travelRule_OPENVASP, str, ],
        travelRule_USTRAVELRULEWG: typing.Union[MetaOapg.properties.travelRule_USTRAVELRULEWG, str, ],
        unit: typing.Union[MetaOapg.properties.unit, str, ],
        otherNames: typing.Union[MetaOapg.properties.otherNames, str, ],
        certificates: typing.Union[MetaOapg.properties.certificates, str, ],
        lastSentDate: typing.Union[MetaOapg.properties.lastSentDate, str, ],
        createdBy: typing.Union[MetaOapg.properties.createdBy, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        postCode: typing.Union[MetaOapg.properties.postCode, str, ],
        did: typing.Union[MetaOapg.properties.did, str, ],
        incorporationCountry: typing.Union[MetaOapg.properties.incorporationCountry, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TravelRuleVASP':
        return super().__new__(
            cls,
            *_args,
            country=country,
            travelRule_TRISA=travelRule_TRISA,
            isNotifiable=isNotifiable,
            travelRule_TRP=travelRule_TRP,
            city=city,
            documents=documents,
            isRegulated=isRegulated,
            travelRule_EMAIL=travelRule_EMAIL,
            description=description,
            identificationType=identificationType,
            identificationCountry=identificationCountry,
            travelRule_SYGNA=travelRule_SYGNA,
            lastReceivedDate=lastReceivedDate,
            legalName=legalName,
            createdAt=createdAt,
            number=number,
            legalStructure=legalStructure,
            street=street,
            travelRule_SHYFT=travelRule_SHYFT,
            regulatoryAuthorities=regulatoryAuthorities,
            addressLine1=addressLine1,
            logo=logo,
            addressLine2=addressLine2,
            state=state,
            jurisdictions=jurisdictions,
            travelRule_TRLIGHT=travelRule_TRLIGHT,
            updatedAt=updatedAt,
            hasAdmin=hasAdmin,
            website=website,
            updatedBy=updatedBy,
            verificationStatus=verificationStatus,
            emailDomains=emailDomains,
            businessNumber=businessNumber,
            issuers=issuers,
            yearFounded=yearFounded,
            travelRule_OPENVASP=travelRule_OPENVASP,
            travelRule_USTRAVELRULEWG=travelRule_USTRAVELRULEWG,
            unit=unit,
            otherNames=otherNames,
            certificates=certificates,
            lastSentDate=lastSentDate,
            createdBy=createdBy,
            name=name,
            postCode=postCode,
            did=did,
            incorporationCountry=incorporationCountry,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.travel_rule_issuers import TravelRuleIssuers