# TravelRuleValidatePerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**natural_person** | [**TravelRuleValidateNaturalPerson**](TravelRuleValidateNaturalPerson.md) |  | [optional] 
**legal_person** | [**TravelRuleValidateLegalPerson**](TravelRuleValidateLegalPerson.md) |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_person import TravelRuleValidatePerson

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidatePerson from a JSON string
travel_rule_validate_person_instance = TravelRuleValidatePerson.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidatePerson.to_json())

# convert the object into a dict
travel_rule_validate_person_dict = travel_rule_validate_person_instance.to_dict()
# create an instance of TravelRuleValidatePerson from a dict
travel_rule_validate_person_from_dict = TravelRuleValidatePerson.from_dict(travel_rule_validate_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


