# TravelRuleNaturalNameIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_identifier** | **str** | The primary identifier of the name. The value must be encrypted. | [optional] 
**secondary_identifier** | **str** | The secondary identifier of the name. The value must be encrypted. | [optional] 
**name_identifier_type** | **str** | The type of the name identifier. The value must be encrypted. The value must be one of the following: [LEGL, DBA, TRAD, NICK, ALIA, MAID, FORM, PREV, BORN, OTHR]. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_natural_name_identifier import TravelRuleNaturalNameIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleNaturalNameIdentifier from a JSON string
travel_rule_natural_name_identifier_instance = TravelRuleNaturalNameIdentifier.from_json(json)
# print the JSON string representation of the object
print(TravelRuleNaturalNameIdentifier.to_json())

# convert the object into a dict
travel_rule_natural_name_identifier_dict = travel_rule_natural_name_identifier_instance.to_dict()
# create an instance of TravelRuleNaturalNameIdentifier from a dict
travel_rule_natural_name_identifier_from_dict = TravelRuleNaturalNameIdentifier.from_dict(travel_rule_natural_name_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


