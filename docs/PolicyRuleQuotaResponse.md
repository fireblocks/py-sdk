# PolicyRuleQuotaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The calculated Amount Over Time (AOT) quota for the rule | [optional] 
**quota_config** | [**AmountOverTimeConfig**](AmountOverTimeConfig.md) |  | [optional] 
**currency** | **str** | The currency of the AOT amount | [optional] 
**window_start** | **float** | Unix timestamp (seconds) of the start of the current AOT time window | [optional] 
**window_end** | **float** | Unix timestamp (seconds) of the end of the current AOT time window (when the AOT was calculated) | [optional] 
**transaction_count** | **float** | Number of transactions in the current AOT time window | [optional] 

## Example

```python
from fireblocks.models.policy_rule_quota_response import PolicyRuleQuotaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleQuotaResponse from a JSON string
policy_rule_quota_response_instance = PolicyRuleQuotaResponse.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleQuotaResponse.to_json())

# convert the object into a dict
policy_rule_quota_response_dict = policy_rule_quota_response_instance.to_dict()
# create an instance of PolicyRuleQuotaResponse from a dict
policy_rule_quota_response_from_dict = PolicyRuleQuotaResponse.from_dict(policy_rule_quota_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


