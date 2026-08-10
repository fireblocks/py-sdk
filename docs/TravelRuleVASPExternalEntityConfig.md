# TravelRuleVASPExternalEntityConfig

An entity record for the VASP as resolved from an external registry, together with the registration state reported by that registry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The external registry the record was resolved from. Returned in lower case, for example &#x60;gleif&#x60;. | [optional] 
**external_id** | **str** | The VASP&#39;s identifier within the external registry. For the &#x60;gleif&#x60; provider this is the Legal Entity Identifier (LEI). | [optional] 
**updated_at** | **str** | Timestamp of the last change to the record at the external registry. | [optional] 
**resolved_at** | **str** | Timestamp when the record was last resolved from the external registry. | [optional] 
**entity** | [**TravelRuleVASPExternalEntity**](TravelRuleVASPExternalEntity.md) |  | [optional] 
**registration** | [**TravelRuleVASPExternalEntityRegistration**](TravelRuleVASPExternalEntityRegistration.md) |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_vasp_external_entity_config import TravelRuleVASPExternalEntityConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleVASPExternalEntityConfig from a JSON string
travel_rule_vasp_external_entity_config_instance = TravelRuleVASPExternalEntityConfig.from_json(json)
# print the JSON string representation of the object
print(TravelRuleVASPExternalEntityConfig.to_json())

# convert the object into a dict
travel_rule_vasp_external_entity_config_dict = travel_rule_vasp_external_entity_config_instance.to_dict()
# create an instance of TravelRuleVASPExternalEntityConfig from a dict
travel_rule_vasp_external_entity_config_from_dict = TravelRuleVASPExternalEntityConfig.from_dict(travel_rule_vasp_external_entity_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


