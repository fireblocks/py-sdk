# LegacyPolicyRuleOperators

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
from fireblocks.models.legacy_policy_rule_operators import LegacyPolicyRuleOperators

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRuleOperators from a JSON string
legacy_policy_rule_operators_instance = LegacyPolicyRuleOperators.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRuleOperators.to_json())

# convert the object into a dict
legacy_policy_rule_operators_dict = legacy_policy_rule_operators_instance.to_dict()
# create an instance of LegacyPolicyRuleOperators from a dict
legacy_policy_rule_operators_from_dict = LegacyPolicyRuleOperators.from_dict(legacy_policy_rule_operators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


