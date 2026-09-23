# Rule

A single rule within a rule set. The first rule whose conditions match wins, and its `ruleAction` is applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | UUID, unique within the rule set. | [optional] 
**conditions** | [**List[RuleCondition]**](RuleCondition.md) | Conditions AND-ed together within this rule. | [optional] 
**rule_action** | [**RuleActionEnum**](RuleActionEnum.md) |  | [optional] 
**order** | **int** | Zero-based evaluation order among the rule set&#39;s rules, lowest first. | [optional] 
**title** | **str** | User-facing label for the rule. Cosmetic only — not read by rule evaluation. | [optional] 

## Example

```python
from fireblocks.models.rule import Rule

# TODO update the JSON string below
json = "{}"
# create an instance of Rule from a JSON string
rule_instance = Rule.from_json(json)
# print the JSON string representation of the object
print(Rule.to_json())

# convert the object into a dict
rule_dict = rule_instance.to_dict()
# create an instance of Rule from a dict
rule_from_dict = Rule.from_dict(rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


