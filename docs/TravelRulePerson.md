# TravelRulePerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**natural_person** | [**TravelRuleNaturalPerson**](TravelRuleNaturalPerson.md) |  | [optional] 
**legal_person** | [**TravelRuleLegalPerson**](TravelRuleLegalPerson.md) |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_person import TravelRulePerson

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRulePerson from a JSON string
travel_rule_person_instance = TravelRulePerson.from_json(json)
# print the JSON string representation of the object
print(TravelRulePerson.to_json())

# convert the object into a dict
travel_rule_person_dict = travel_rule_person_instance.to_dict()
# create an instance of TravelRulePerson from a dict
travel_rule_person_from_dict = TravelRulePerson.from_dict(travel_rule_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


