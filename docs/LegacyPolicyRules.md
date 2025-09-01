# LegacyPolicyRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[LegacyPolicyRule]**](LegacyPolicyRule.md) | Policy rules | [optional] 

## Example

```python
from fireblocks.models.legacy_policy_rules import LegacyPolicyRules

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRules from a JSON string
legacy_policy_rules_instance = LegacyPolicyRules.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRules.to_json())

# convert the object into a dict
legacy_policy_rules_dict = legacy_policy_rules_instance.to_dict()
# create an instance of LegacyPolicyRules from a dict
legacy_policy_rules_from_dict = LegacyPolicyRules.from_dict(legacy_policy_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


