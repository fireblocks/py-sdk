# LegacyPolicyRuleSrc

Defines source accounts the rule allows transfers to originate from

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[List[LegacySrcOrDestAttributesInner]]** | A set of ids in a tuple format | [optional] 

## Example

```python
from fireblocks.models.legacy_policy_rule_src import LegacyPolicyRuleSrc

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRuleSrc from a JSON string
legacy_policy_rule_src_instance = LegacyPolicyRuleSrc.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRuleSrc.to_json())

# convert the object into a dict
legacy_policy_rule_src_dict = legacy_policy_rule_src_instance.to_dict()
# create an instance of LegacyPolicyRuleSrc from a dict
legacy_policy_rule_src_from_dict = LegacyPolicyRuleSrc.from_dict(legacy_policy_rule_src_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


