# RuleCondition

A single condition within a rule. Conditions within a rule are AND-ed together.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The input context field this condition tests. Allowed values depend on the rule set type (trigger vs. outcome) and the step&#39;s connector/operation. | 
**operator** | [**RuleConditionOperatorEnum**](RuleConditionOperatorEnum.md) |  | 
**value** | **str** | The value &#x60;field&#x60; is compared against, using &#x60;operator&#x60;. | 

## Example

```python
from fireblocks.models.rule_condition import RuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of RuleCondition from a JSON string
rule_condition_instance = RuleCondition.from_json(json)
# print the JSON string representation of the object
print(RuleCondition.to_json())

# convert the object into a dict
rule_condition_dict = rule_condition_instance.to_dict()
# create an instance of RuleCondition from a dict
rule_condition_from_dict = RuleCondition.from_dict(rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


