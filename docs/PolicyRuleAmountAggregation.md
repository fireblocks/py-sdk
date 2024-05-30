# PolicyRuleAmountAggregation

Defines the method by which the Policy Engine calculates accumulation. It uses the Initiator, Source, and Destination to calculate accumulation toward the value under Minimum, for the time under Time Period. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operators** | [**AmountAggregationTimePeriodMethod**](AmountAggregationTimePeriodMethod.md) |  | [optional] 
**src_transfer_peers** | [**AmountAggregationTimePeriodMethod**](AmountAggregationTimePeriodMethod.md) |  | [optional] 
**dst_transfer_peers** | [**AmountAggregationTimePeriodMethod**](AmountAggregationTimePeriodMethod.md) |  | [optional] 

## Example

```python
from fireblocks.models.policy_rule_amount_aggregation import PolicyRuleAmountAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleAmountAggregation from a JSON string
policy_rule_amount_aggregation_instance = PolicyRuleAmountAggregation.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleAmountAggregation.to_json())

# convert the object into a dict
policy_rule_amount_aggregation_dict = policy_rule_amount_aggregation_instance.to_dict()
# create an instance of PolicyRuleAmountAggregation from a dict
policy_rule_amount_aggregation_from_dict = PolicyRuleAmountAggregation.from_dict(policy_rule_amount_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


