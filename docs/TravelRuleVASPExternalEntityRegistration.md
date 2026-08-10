# TravelRuleVASPExternalEntityRegistration

The registration state of the VASP as reported by an external registry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The registration status at the external registry, for example &#x60;ISSUED&#x60;, &#x60;LAPSED&#x60; or &#x60;RETIRED&#x60;. The value set is defined by the registry, not by Fireblocks. | [optional] 
**next_renewal_date** | **str** | The date the registration is next due for renewal at the external registry. | [optional] 
**corroboration_level** | **str** | The level to which the registry has corroborated the entity data, for example &#x60;FULLY_CORROBORATED&#x60;. The value set is defined by the registry, not by Fireblocks. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_vasp_external_entity_registration import TravelRuleVASPExternalEntityRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleVASPExternalEntityRegistration from a JSON string
travel_rule_vasp_external_entity_registration_instance = TravelRuleVASPExternalEntityRegistration.from_json(json)
# print the JSON string representation of the object
print(TravelRuleVASPExternalEntityRegistration.to_json())

# convert the object into a dict
travel_rule_vasp_external_entity_registration_dict = travel_rule_vasp_external_entity_registration_instance.to_dict()
# create an instance of TravelRuleVASPExternalEntityRegistration from a dict
travel_rule_vasp_external_entity_registration_from_dict = TravelRuleVASPExternalEntityRegistration.from_dict(travel_rule_vasp_external_entity_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


