# TravelRuleVASPExternalEntity

The VASP's entity data as held by an external registry. These fields mirror a subset of the top-level VASP fields, but carry the registry's values rather than the VASP's own, so the two may differ.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** | The legal name of the entity as recorded by the external registry. | [optional] 
**other_legal_name** | **str** | Alternative legal names of the entity, as a comma-separated list. | [optional] 
**legal_form** | **str** | The Entity Legal Form (ELF) code of the entity. | [optional] 
**legal_structure** | **str** | The legal structure of the entity. The external registry may return the Entity Legal Form code in this field, so its value can duplicate &#x60;legalForm&#x60;. | [optional] 
**entity_category** | **str** | The category assigned to the entity by the external registry. | [optional] 
**entity_status** | **str** | The status of the entity at the external registry. | [optional] 
**business_number** | **str** | The business registration number of the entity. | [optional] 
**year_founded** | **str** | The year the entity was founded. Returned as a string, not an integer. | [optional] 
**jurisdictions** | **str** | The jurisdictions the entity is registered in. | [optional] 
**address_line1** | **str** | The first line of the entity&#39;s registered address. | [optional] 
**number** | **str** | The building number of the entity&#39;s registered address. May be returned as an empty string as well as &#x60;null&#x60; when not supplied. | [optional] 
**post_code** | **str** | The postal code of the entity&#39;s registered address. | [optional] 
**city** | **str** | The city of the entity&#39;s registered address. | [optional] 
**state** | **str** | The state or region of the entity&#39;s registered address, as an ISO-3166-2 subdivision code. | [optional] 
**country** | **str** | The country of the entity&#39;s registered address (ISO-3166 Alpha-2 code). | [optional] 
**hq_street** | **str** | The street of the entity&#39;s headquarters address. | [optional] 
**hq_number** | **str** | The building number of the entity&#39;s headquarters address. May be returned as an empty string as well as &#x60;null&#x60; when not supplied. | [optional] 
**hq_postcode** | **str** | The postal code of the entity&#39;s headquarters address. | [optional] 
**hq_city** | **str** | The city of the entity&#39;s headquarters address. | [optional] 
**hq_region** | **str** | The region of the entity&#39;s headquarters address, as an ISO-3166-2 subdivision code. | [optional] 
**hq_country** | **str** | The country of the entity&#39;s headquarters address (ISO-3166 Alpha-2 code). | [optional] 

## Example

```python
from fireblocks.models.travel_rule_vasp_external_entity import TravelRuleVASPExternalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleVASPExternalEntity from a JSON string
travel_rule_vasp_external_entity_instance = TravelRuleVASPExternalEntity.from_json(json)
# print the JSON string representation of the object
print(TravelRuleVASPExternalEntity.to_json())

# convert the object into a dict
travel_rule_vasp_external_entity_dict = travel_rule_vasp_external_entity_instance.to_dict()
# create an instance of TravelRuleVASPExternalEntity from a dict
travel_rule_vasp_external_entity_from_dict = TravelRuleVASPExternalEntity.from_dict(travel_rule_vasp_external_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


