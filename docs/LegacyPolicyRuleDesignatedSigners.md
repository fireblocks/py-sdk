# LegacyPolicyRuleDesignatedSigners

Set of ids representing the users who signs transactions that match a specific rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | Set of users ids | [optional] 
**users_groups** | **List[str]** | Set of group ids | [optional] 

## Example

```python
from fireblocks.models.legacy_policy_rule_designated_signers import LegacyPolicyRuleDesignatedSigners

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRuleDesignatedSigners from a JSON string
legacy_policy_rule_designated_signers_instance = LegacyPolicyRuleDesignatedSigners.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRuleDesignatedSigners.to_json())

# convert the object into a dict
legacy_policy_rule_designated_signers_dict = legacy_policy_rule_designated_signers_instance.to_dict()
# create an instance of LegacyPolicyRuleDesignatedSigners from a dict
legacy_policy_rule_designated_signers_from_dict = LegacyPolicyRuleDesignatedSigners.from_dict(legacy_policy_rule_designated_signers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


