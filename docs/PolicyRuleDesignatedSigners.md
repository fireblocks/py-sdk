# PolicyRuleDesignatedSigners

Set of ids representing the users who signs transactions that match a specific rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | Set of users ids | [optional] 
**users_groups** | **List[str]** | Set of group ids | [optional] 

## Example

```python
from fireblocks.models.policy_rule_designated_signers import PolicyRuleDesignatedSigners

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleDesignatedSigners from a JSON string
policy_rule_designated_signers_instance = PolicyRuleDesignatedSigners.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleDesignatedSigners.to_json())

# convert the object into a dict
policy_rule_designated_signers_dict = policy_rule_designated_signers_instance.to_dict()
# create an instance of PolicyRuleDesignatedSigners from a dict
policy_rule_designated_signers_from_dict = PolicyRuleDesignatedSigners.from_dict(policy_rule_designated_signers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


