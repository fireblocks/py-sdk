# LegalEntityRegistration

Legal entity registration record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique registration identifier | 
**lei** | **str** | Legal Entity Identifier (LEI) code | 
**status** | [**LeiStatus**](LeiStatus.md) |  | 
**is_default** | **bool** | Whether this is the default legal entity for the workspace | 
**travel_rule_providers** | [**List[TravelRuleProvider]**](TravelRuleProvider.md) | Travel rule providers configured for this registration | 
**travel_rule_contact_email** | **str** | Contact email for travel rule communications | [optional] 
**gleif_data** | [**GleifData**](GleifData.md) |  | [optional] 
**created_at** | **str** | Creation timestamp in milliseconds since epoch | 
**updated_at** | **str** | Last update timestamp in milliseconds since epoch | 

## Example

```python
from fireblocks.models.legal_entity_registration import LegalEntityRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of LegalEntityRegistration from a JSON string
legal_entity_registration_instance = LegalEntityRegistration.from_json(json)
# print the JSON string representation of the object
print(LegalEntityRegistration.to_json())

# convert the object into a dict
legal_entity_registration_dict = legal_entity_registration_instance.to_dict()
# create an instance of LegalEntityRegistration from a dict
legal_entity_registration_from_dict = LegalEntityRegistration.from_dict(legal_entity_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


