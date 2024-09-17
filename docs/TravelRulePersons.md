# TravelRulePersons


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**natural_person** | [**TravelRuleNaturalPerson**](TravelRuleNaturalPerson.md) |  | [optional] 
**legal_person** | [**TravelRuleLegalPerson**](TravelRuleLegalPerson.md) |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_persons import TravelRulePersons

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRulePersons from a JSON string
travel_rule_persons_instance = TravelRulePersons.from_json(json)
# print the JSON string representation of the object
print(TravelRulePersons.to_json())

# convert the object into a dict
travel_rule_persons_dict = travel_rule_persons_instance.to_dict()
# create an instance of TravelRulePersons from a dict
travel_rule_persons_from_dict = TravelRulePersons.from_dict(travel_rule_persons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


