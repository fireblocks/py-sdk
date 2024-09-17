# TravelRuleNaturalNameIdentifiers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_identifier** | **str** |  | [optional] 
**secondary_identifier** | **str** |  | [optional] 
**name_identifier_type** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_natural_name_identifiers import TravelRuleNaturalNameIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleNaturalNameIdentifiers from a JSON string
travel_rule_natural_name_identifiers_instance = TravelRuleNaturalNameIdentifiers.from_json(json)
# print the JSON string representation of the object
print(TravelRuleNaturalNameIdentifiers.to_json())

# convert the object into a dict
travel_rule_natural_name_identifiers_dict = travel_rule_natural_name_identifiers_instance.to_dict()
# create an instance of TravelRuleNaturalNameIdentifiers from a dict
travel_rule_natural_name_identifiers_from_dict = TravelRuleNaturalNameIdentifiers.from_dict(travel_rule_natural_name_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


