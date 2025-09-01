# LegacyPolicyRuleDst

Defines the destination accounts the rule allows transfers to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[List[LegacySrcOrDestAttributesInner]]** | A set of ids in a tuple format | [optional] 

## Example

```python
from fireblocks.models.legacy_policy_rule_dst import LegacyPolicyRuleDst

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRuleDst from a JSON string
legacy_policy_rule_dst_instance = LegacyPolicyRuleDst.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRuleDst.to_json())

# convert the object into a dict
legacy_policy_rule_dst_dict = legacy_policy_rule_dst_instance.to_dict()
# create an instance of LegacyPolicyRuleDst from a dict
legacy_policy_rule_dst_from_dict = LegacyPolicyRuleDst.from_dict(legacy_policy_rule_dst_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


