# PolicyRuleQuotaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The ID of the policy rule to calculate AOT quota for | 
**initiator** | **str** | Optional initiator identifier for the AOT calculation | [optional] 
**source** | [**PolicyRuleQuotaParticipant**](PolicyRuleQuotaParticipant.md) |  | [optional] 
**destination** | [**PolicyRuleQuotaParticipant**](PolicyRuleQuotaParticipant.md) |  | [optional] 

## Example

```python
from fireblocks.models.policy_rule_quota_request import PolicyRuleQuotaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleQuotaRequest from a JSON string
policy_rule_quota_request_instance = PolicyRuleQuotaRequest.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleQuotaRequest.to_json())

# convert the object into a dict
policy_rule_quota_request_dict = policy_rule_quota_request_instance.to_dict()
# create an instance of PolicyRuleQuotaRequest from a dict
policy_rule_quota_request_from_dict = PolicyRuleQuotaRequest.from_dict(policy_rule_quota_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


