# LegacyPolicyRuleAuthorizationGroupsGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | User ids | [optional] 
**users_groups** | **List[str]** | Group ids | [optional] 
**th** | **float** | Represents the min amount of entities which are required to approve the transaction, default is 1. | [optional] 

## Example

```python
from fireblocks.models.legacy_policy_rule_authorization_groups_groups_inner import LegacyPolicyRuleAuthorizationGroupsGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRuleAuthorizationGroupsGroupsInner from a JSON string
legacy_policy_rule_authorization_groups_groups_inner_instance = LegacyPolicyRuleAuthorizationGroupsGroupsInner.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRuleAuthorizationGroupsGroupsInner.to_json())

# convert the object into a dict
legacy_policy_rule_authorization_groups_groups_inner_dict = legacy_policy_rule_authorization_groups_groups_inner_instance.to_dict()
# create an instance of LegacyPolicyRuleAuthorizationGroupsGroupsInner from a dict
legacy_policy_rule_authorization_groups_groups_inner_from_dict = LegacyPolicyRuleAuthorizationGroupsGroupsInner.from_dict(legacy_policy_rule_authorization_groups_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


