# PolicyRuleAmount

Defines the value a transaction must exceed for the rule to apply to it (according to the amountCurrency field)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fireblocks.models.policy_rule_amount import PolicyRuleAmount

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleAmount from a JSON string
policy_rule_amount_instance = PolicyRuleAmount.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleAmount.to_json())

# convert the object into a dict
policy_rule_amount_dict = policy_rule_amount_instance.to_dict()
# create an instance of PolicyRuleAmount from a dict
policy_rule_amount_from_dict = PolicyRuleAmount.from_dict(policy_rule_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


