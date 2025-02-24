# TravelRuleValidateNaturalPersonNameIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_identifier** | [**List[TravelRuleValidateNaturalNameIdentifier]**](TravelRuleValidateNaturalNameIdentifier.md) |  | [optional] 
**local_name_identifier** | [**List[TravelRuleValidateNaturalNameIdentifier]**](TravelRuleValidateNaturalNameIdentifier.md) |  | [optional] 
**phonetic_name_identifier** | [**List[TravelRuleValidateNaturalNameIdentifier]**](TravelRuleValidateNaturalNameIdentifier.md) |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_natural_person_name_identifier import TravelRuleValidateNaturalPersonNameIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateNaturalPersonNameIdentifier from a JSON string
travel_rule_validate_natural_person_name_identifier_instance = TravelRuleValidateNaturalPersonNameIdentifier.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateNaturalPersonNameIdentifier.to_json())

# convert the object into a dict
travel_rule_validate_natural_person_name_identifier_dict = travel_rule_validate_natural_person_name_identifier_instance.to_dict()
# create an instance of TravelRuleValidateNaturalPersonNameIdentifier from a dict
travel_rule_validate_natural_person_name_identifier_from_dict = TravelRuleValidateNaturalPersonNameIdentifier.from_dict(travel_rule_validate_natural_person_name_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


