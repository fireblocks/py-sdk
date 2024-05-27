# PolicyRuleSrc

Defines source accounts the rule allows transfers to originate from

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[List[SrcOrDestAttributesInner]]** | A set of ids in a tuple format | [optional] 

## Example

```python
from fireblocks_client.models.policy_rule_src import PolicyRuleSrc

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleSrc from a JSON string
policy_rule_src_instance = PolicyRuleSrc.from_json(json)
# print the JSON string representation of the object
print PolicyRuleSrc.to_json()

# convert the object into a dict
policy_rule_src_dict = policy_rule_src_instance.to_dict()
# create an instance of PolicyRuleSrc from a dict
policy_rule_src_form_dict = policy_rule_src.from_dict(policy_rule_src_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


