# LegacyPolicyRuleAmount

Defines the value a transaction must exceed for the rule to apply to it (according to the amountCurrency field)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fireblocks.models.legacy_policy_rule_amount import LegacyPolicyRuleAmount

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRuleAmount from a JSON string
legacy_policy_rule_amount_instance = LegacyPolicyRuleAmount.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRuleAmount.to_json())

# convert the object into a dict
legacy_policy_rule_amount_dict = legacy_policy_rule_amount_instance.to_dict()
# create an instance of LegacyPolicyRuleAmount from a dict
legacy_policy_rule_amount_from_dict = LegacyPolicyRuleAmount.from_dict(legacy_policy_rule_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


