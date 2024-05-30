# TravelRulePolicyRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** |  | [optional] 
**source_sub_type** | **str** |  | [optional] 
**dest_type** | **str** |  | [optional] 
**dest_sub_type** | **str** |  | [optional] 
**dest_address** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**dest_id** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**base_asset** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**amount_usd** | **float** |  | [optional] 
**network_protocol** | **str** |  | [optional] 
**operation** | **str** |  | [optional] 
**action** | **str** |  | 

## Example

```python
from fireblocks.models.travel_rule_policy_rule_response import TravelRulePolicyRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRulePolicyRuleResponse from a JSON string
travel_rule_policy_rule_response_instance = TravelRulePolicyRuleResponse.from_json(json)
# print the JSON string representation of the object
print(TravelRulePolicyRuleResponse.to_json())

# convert the object into a dict
travel_rule_policy_rule_response_dict = travel_rule_policy_rule_response_instance.to_dict()
# create an instance of TravelRulePolicyRuleResponse from a dict
travel_rule_policy_rule_response_from_dict = TravelRulePolicyRuleResponse.from_dict(travel_rule_policy_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


