# LegacyPolicyRuleAmountAggregation

Defines the method by which the Policy Engine calculates accumulation. It uses the Initiator, Source, and Destination to calculate accumulation toward the value under Minimum, for the time under Time Period. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operators** | [**LegacyAmountAggregationTimePeriodMethod**](LegacyAmountAggregationTimePeriodMethod.md) |  | [optional] 
**src_transfer_peers** | [**LegacyAmountAggregationTimePeriodMethod**](LegacyAmountAggregationTimePeriodMethod.md) |  | [optional] 
**dst_transfer_peers** | [**LegacyAmountAggregationTimePeriodMethod**](LegacyAmountAggregationTimePeriodMethod.md) |  | [optional] 

## Example

```python
from fireblocks.models.legacy_policy_rule_amount_aggregation import LegacyPolicyRuleAmountAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRuleAmountAggregation from a JSON string
legacy_policy_rule_amount_aggregation_instance = LegacyPolicyRuleAmountAggregation.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRuleAmountAggregation.to_json())

# convert the object into a dict
legacy_policy_rule_amount_aggregation_dict = legacy_policy_rule_amount_aggregation_instance.to_dict()
# create an instance of LegacyPolicyRuleAmountAggregation from a dict
legacy_policy_rule_amount_aggregation_from_dict = LegacyPolicyRuleAmountAggregation.from_dict(legacy_policy_rule_amount_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


