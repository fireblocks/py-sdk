# TravelRuleVASP

A VASP record from the Travel Rule trust framework directory.  The set of keys returned depends on the `fields` query parameter. When `fields` is omitted, or supplied with an empty value, this endpoint returns the complete record.  Additional fields may be present in the response beyond those documented here. Clients must ignore unrecognised fields rather than failing to deserialize.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**did** | **str** | The Decentralized Identifier (DID) of the VASP. | 
**name** | **str** | The name of the VASP. | 
**verification_status** | **str** | The current verification status of the VASP. | 
**address_line1** | **str** | The first line of the VASP&#39;s address. | 
**address_line2** | **str** | The second line of the VASP&#39;s address (if applicable). May be null. | [optional] 
**city** | **str** | The city where the VASP is located. | 
**country** | **str** | The country where the VASP is registered (ISO-3166 Alpha-2 code). | 
**email_domains** | **str** | The email domains associated with the VASP. The field&#39;s type is string; its content is a JSON-encoded array of domains. Clients must parse this value to obtain the array. | 
**website** | **str** | The official website of the VASP. | 
**logo** | **str** | URL to the logo of the VASP. May be null. | [optional] 
**legal_structure** | **str** | The legal structure of the VASP (e.g., Corporation, LLC). | 
**legal_name** | **str** | The legal name of the VASP. | 
**year_founded** | **str** | The year the VASP was founded. Returned as a string, not an integer. | 
**incorporation_country** | **str** | The country where the VASP is incorporated (ISO-3166 Alpha-2 code). | 
**is_regulated** | **str** | Indicates whether the VASP is regulated. | 
**other_names** | **str** | Other names the VASP is known by. May be null. | [optional] 
**identification_type** | **str** | The type of identification used by the VASP. | [optional] 
**identification_country** | **str** | The country of identification for the VASP (ISO-3166 Alpha-2 code). May be null. | [optional] 
**business_number** | **str** | The business registration number of the VASP. | [optional] 
**regulatory_authorities** | **str** | The regulatory authorities overseeing the VASP. May be null. | [optional] 
**jurisdictions** | **str** | The jurisdictions where the VASP operates. | 
**division** | **str** | The division of the VASP&#39;s registered address, where applicable. | [optional] 
**street** | **str** | The street name where the VASP is located. May be null. | [optional] 
**number** | **str** | The building number of the VASP&#39;s address. May be returned as an empty string when not supplied. | [optional] 
**unit** | **str** | The unit or suite number of the VASP&#39;s address. May be null. | [optional] 
**post_code** | **str** | The postal code of the VASP&#39;s location. | [optional] 
**state** | **str** | The state or region where the VASP is located. | [optional] 
**other_legal_name** | **str** | Alternative legal names of the VASP, as a comma-separated list. Resolved from an external registry, so it is only populated for VASPs with a resolved entity record. | [optional] 
**gleif_updated_at** | **str** | Timestamp of the last synchronization with the GLEIF registry. Only populated for VASPs with a GLEIF-resolved LEI. | [optional] 
**lei_number** | **str** | The VASP&#39;s Legal Entity Identifier (LEI), a 20-character alphanumeric code. Only populated for VASPs with a GLEIF-resolved LEI. | [optional] 
**legal_form** | **str** | The GLEIF Entity Legal Form (ELF) code of the VASP. Only populated for VASPs with a GLEIF-resolved LEI. | [optional] 
**entity_category** | **str** | The GLEIF entity category of the VASP. Only populated for VASPs with a GLEIF-resolved LEI. | [optional] 
**entity_status** | **str** | The GLEIF entity status of the VASP. Only populated for VASPs with a GLEIF-resolved LEI. | [optional] 
**external_entity_config** | [**List[TravelRuleVASPExternalEntityConfig]**](TravelRuleVASPExternalEntityConfig.md) | Entity records resolved from external registries, such as GLEIF. Only populated for VASPs that have been resolved against at least one external registry. | [optional] 
**hq_street** | **str** | The street of the VASP&#39;s headquarters address. Only populated for VASPs with a GLEIF-resolved LEI. | [optional] 
**hq_number** | **str** | The building number of the VASP&#39;s headquarters address. May be returned as an empty string as well as &#x60;null&#x60; when not supplied. | [optional] 
**hq_postcode** | **str** | The postal code of the VASP&#39;s headquarters address. Only populated for VASPs with a GLEIF-resolved LEI. | [optional] 
**hq_region** | **str** | The region of the VASP&#39;s headquarters address, as an ISO-3166-2 subdivision code. Only populated for VASPs with a GLEIF-resolved LEI. | [optional] 
**hq_city** | **str** | The city of the VASP&#39;s headquarters address. Only populated for VASPs with a GLEIF-resolved LEI. | [optional] 
**hq_country** | **str** | The country of the VASP&#39;s headquarters address (ISO-3166 Alpha-2 code). Only populated for VASPs with a GLEIF-resolved LEI. | [optional] 
**certificates** | **str** | Certificates or licenses held by the VASP. May be null. | [optional] 
**description** | **str** | A brief description of the VASP. May be null. | [optional] 
**travel_rule_openvasp** | **str** | Travel rule compliance status for OpenVASP. Null when the VASP does not support this protocol. | [optional] 
**travel_rule_sygna** | **str** | Travel rule compliance status for Sygna. Null when the VASP does not support this protocol. | [optional] 
**travel_rule_trisa** | **str** | Travel rule compliance status for TRISA. Null when the VASP does not support this protocol. | [optional] 
**travel_rule_trlight** | **str** | Travel rule compliance status for TRLight. | 
**travel_rule_email** | **str** | Travel rule compliance status for EMAIL. Null when the VASP does not support this protocol. | [optional] 
**travel_rule_trp** | **str** | Travel rule compliance status for TRP. Null when the VASP does not support this protocol. | [optional] 
**travel_rule_shyft** | **str** | Travel rule compliance status for Shyft. Null when the VASP does not support this protocol. | [optional] 
**travel_rule_ustravelrulewg** | **str** | Travel rule compliance status for US Travel Rule WG. Null when the VASP does not support this protocol. | [optional] 
**created_at** | **str** | Timestamp when the VASP record was created. | 
**created_by** | **str** | The DID of the party that created the VASP record. May be null. | [optional] 
**updated_at** | **str** | Timestamp of the last update to the VASP record. | [optional] 
**updated_by** | **str** | The DID of the party that last updated the VASP record. | [optional] 
**last_sent_date** | **str** | The last date a transaction was sent by the VASP. | [optional] 
**last_received_date** | **str** | The last date a transaction was received by the VASP. | [optional] 
**documents** | **str** | Documents associated with the VASP. May be null. | [optional] 
**has_admin** | **bool** | Indicates if the VASP has an admin. | 
**is_notifiable** | **bool** | Indicates if the VASP is notifiable for compliance reasons. | 
**issuers** | [**TravelRuleIssuers**](TravelRuleIssuers.md) |  | 
**regulatory_status** | **str** | The regulatory status of the VASP, as free text. | [optional] 
**supervisory_authority** | **str** | The supervisory authority responsible for the VASP. | [optional] 
**registration_license_id** | **str** | The identifier of the VASP&#39;s registration or operating license. | [optional] 
**status_start_date** | **str** | The date the VASP&#39;s current regulatory status took effect. | [optional] 
**status_expiration_date** | **str** | The date the VASP&#39;s current regulatory status expires. | [optional] 
**last_checked** | **str** | Timestamp of the last verification of the VASP&#39;s regulatory status. | [optional] 
**additional_information** | **str** | Additional free-text information about the VASP. | [optional] 
**subsidiary_of** | **str** | The DID of the parent VASP, when this VASP is a subsidiary of another. | [optional] 
**pii_didkey** | **str** | The VASP&#39;s public PII encryption key, published in the trust framework directory. Use it to encrypt IVMS101 personally identifiable information addressed to this VASP. | [optional] 
**compliance_phase** | **int** | The VASP&#39;s current compliance onboarding phase. | [optional] 
**compliance_phase_data** | **Dict[str, bool]** | The VASP&#39;s progress through the Travel Rule compliance onboarding milestones, as a map keyed by milestone code.  Each value indicates whether that milestone has been completed. The set of milestone codes is defined by the Travel Rule provider and may change over time, so clients must not assume any particular key is present. Examples of milestone codes include &#x60;TX_SENT&#x60;, &#x60;TX_NOTIFY_API&#x60;, &#x60;TF_VASP_VERIFIED&#x60;, &#x60;RULES_CUSTOM_INCOMING&#x60; and &#x60;INTEGRATIONS_WIDGET&#x60;. | [optional] 
**vaspnet_id** | **str** | The VASP&#39;s VASPnet identifier. | [optional] 
**vaspnet_updated_at** | **str** | Timestamp of the last synchronization with VASPnet. | [optional] 
**vaspnet_immutable_fields** | **List[str]** | Names of the fields that are managed by VASPnet and cannot be modified locally. Empty when no fields are locked. | [optional] 
**node_didkey** | **str** | The public key of the Travel Rule node serving this VASP record. The format has not been confirmed against a live response; every observed value has been null. | [optional] 
**ddq** | **str** | The VASP&#39;s Due Diligence Questionnaire, as a JSON-encoded string containing a &#x60;data&#x60; object and an &#x60;updatedAt&#x60; timestamp. Clients must parse this value. | [optional] 
**target_protocol** | **str** | The Travel Rule protocol used to reach this VASP, when a specific one is configured. | [optional] 
**parent_gateway** | **str** | The DID of the gateway VASP that routes messages on this VASP&#39;s behalf. | [optional] 
**is_active_sender** | **bool** | Indicates if the VASP actively sends Travel Rule transfers. | [optional] 
**is_active_receiver** | **bool** | Indicates if the VASP actively receives Travel Rule transfers. | [optional] 
**subsidiaries** | **List[object]** | The VASP&#39;s subsidiary entities. The element schema is not yet documented, as no response containing a populated value has been observed; do not assume a particular element type. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_vasp import TravelRuleVASP

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleVASP from a JSON string
travel_rule_vasp_instance = TravelRuleVASP.from_json(json)
# print the JSON string representation of the object
print(TravelRuleVASP.to_json())

# convert the object into a dict
travel_rule_vasp_dict = travel_rule_vasp_instance.to_dict()
# create an instance of TravelRuleVASP from a dict
travel_rule_vasp_from_dict = TravelRuleVASP.from_dict(travel_rule_vasp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


