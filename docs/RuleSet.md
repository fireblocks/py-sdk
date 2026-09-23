# RuleSet

An ordered set of rules. Rules are evaluated top to bottom, and the first one that matches wins.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[Rule]**](Rule.md) | Ordered rule list, evaluated top to bottom; the first match wins. | [optional] 

## Example

```python
from fireblocks.models.rule_set import RuleSet

# TODO update the JSON string below
json = "{}"
# create an instance of RuleSet from a JSON string
rule_set_instance = RuleSet.from_json(json)
# print the JSON string representation of the object
print(RuleSet.to_json())

# convert the object into a dict
rule_set_dict = rule_set_instance.to_dict()
# create an instance of RuleSet from a dict
rule_set_from_dict = RuleSet.from_dict(rule_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


