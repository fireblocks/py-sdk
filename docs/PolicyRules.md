# PolicyRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[PolicyRule]**](PolicyRule.md) | Policy rules | [optional] 

## Example

```python
from fireblocks.models.policy_rules import PolicyRules

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRules from a JSON string
policy_rules_instance = PolicyRules.from_json(json)
# print the JSON string representation of the object
print(PolicyRules.to_json())

# convert the object into a dict
policy_rules_dict = policy_rules_instance.to_dict()
# create an instance of PolicyRules from a dict
policy_rules_from_dict = PolicyRules.from_dict(policy_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


