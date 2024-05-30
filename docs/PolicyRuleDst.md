# PolicyRuleDst

Defines the destination accounts the rule allows transfers to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[List[SrcOrDestAttributesInner]]** | A set of ids in a tuple format | [optional] 

## Example

```python
from fireblocks.models.policy_rule_dst import PolicyRuleDst

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleDst from a JSON string
policy_rule_dst_instance = PolicyRuleDst.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleDst.to_json())

# convert the object into a dict
policy_rule_dst_dict = policy_rule_dst_instance.to_dict()
# create an instance of PolicyRuleDst from a dict
policy_rule_dst_from_dict = PolicyRuleDst.from_dict(policy_rule_dst_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


