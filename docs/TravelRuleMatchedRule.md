# TravelRuleMatchedRule

The travel rule configuration that was matched

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**TravelRuleDirectionEnum**](TravelRuleDirectionEnum.md) |  | [optional] 
**status** | [**TravelRuleStatusEnum**](TravelRuleStatusEnum.md) |  | [optional] 
**amount_usd** | **float** | Amount in USD | [optional] 
**amount** | **float** | Amount in base currency | [optional] 
**asset** | **str** | Asset identifier | [optional] 
**action** | [**TravelRuleVerdictEnum**](TravelRuleVerdictEnum.md) |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_matched_rule import TravelRuleMatchedRule

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleMatchedRule from a JSON string
travel_rule_matched_rule_instance = TravelRuleMatchedRule.from_json(json)
# print the JSON string representation of the object
print(TravelRuleMatchedRule.to_json())

# convert the object into a dict
travel_rule_matched_rule_dict = travel_rule_matched_rule_instance.to_dict()
# create an instance of TravelRuleMatchedRule from a dict
travel_rule_matched_rule_from_dict = TravelRuleMatchedRule.from_dict(travel_rule_matched_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


