# PolicyRuleQuotaParticipant

Participant identifier for AOT quota calculation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Participant identifier (integer for VAULT accounts, UUID for others) | 
**type** | **str** | Participant type | 

## Example

```python
from fireblocks.models.policy_rule_quota_participant import PolicyRuleQuotaParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleQuotaParticipant from a JSON string
policy_rule_quota_participant_instance = PolicyRuleQuotaParticipant.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleQuotaParticipant.to_json())

# convert the object into a dict
policy_rule_quota_participant_dict = policy_rule_quota_participant_instance.to_dict()
# create an instance of PolicyRuleQuotaParticipant from a dict
policy_rule_quota_participant_from_dict = PolicyRuleQuotaParticipant.from_dict(policy_rule_quota_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


