# PolicyRuleOperators

Defines users/groups who can initiate the type of transaction to which the rule applies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wildcard** | **str** | If used then this property should appear as the only child property * \&quot;*\&quot; - All users are allowed  | [optional] 
**users** | **List[str]** | Set of users ids | [optional] 
**users_groups** | **List[str]** | Set of group ids | [optional] 
**services** | **List[str]** | set of services to initiate transactions | [optional] 

## Example

```python
from fireblocks.models.policy_rule_operators import PolicyRuleOperators

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleOperators from a JSON string
policy_rule_operators_instance = PolicyRuleOperators.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleOperators.to_json())

# convert the object into a dict
policy_rule_operators_dict = policy_rule_operators_instance.to_dict()
# create an instance of PolicyRuleOperators from a dict
policy_rule_operators_from_dict = PolicyRuleOperators.from_dict(policy_rule_operators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


