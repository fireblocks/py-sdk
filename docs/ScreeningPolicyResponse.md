# ScreeningPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**TravelRulePolicyRuleResponse**](TravelRulePolicyRuleResponse.md) |  | 
**policy_status** | **str** |  | [optional] 
**is_default** | **bool** |  | 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | 

## Example

```python
from fireblocks_client.models.screening_policy_response import ScreeningPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningPolicyResponse from a JSON string
screening_policy_response_instance = ScreeningPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(ScreeningPolicyResponse.to_json())

# convert the object into a dict
screening_policy_response_dict = screening_policy_response_instance.to_dict()
# create an instance of ScreeningPolicyResponse from a dict
screening_policy_response_from_dict = ScreeningPolicyResponse.from_dict(screening_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


