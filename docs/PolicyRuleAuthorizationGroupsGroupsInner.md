# PolicyRuleAuthorizationGroupsGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | User ids | [optional] 
**users_groups** | **List[str]** | Group ids | [optional] 
**th** | **float** | Represents the min amount of entities which are required to approve the transaction, default is 1. | [optional] 

## Example

```python
from fireblocks.models.policy_rule_authorization_groups_groups_inner import PolicyRuleAuthorizationGroupsGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleAuthorizationGroupsGroupsInner from a JSON string
policy_rule_authorization_groups_groups_inner_instance = PolicyRuleAuthorizationGroupsGroupsInner.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleAuthorizationGroupsGroupsInner.to_json())

# convert the object into a dict
policy_rule_authorization_groups_groups_inner_dict = policy_rule_authorization_groups_groups_inner_instance.to_dict()
# create an instance of PolicyRuleAuthorizationGroupsGroupsInner from a dict
policy_rule_authorization_groups_groups_inner_from_dict = PolicyRuleAuthorizationGroupsGroupsInner.from_dict(policy_rule_authorization_groups_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


