# PolicyRuleCheckResult

The rule validation result

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** | Rule index number in the policy | 
**status** | **str** | Validation status | 
**errors** | [**List[PolicyRuleError]**](PolicyRuleError.md) | A set of rule validation error objects | 

## Example

```python
from fireblocks_client.models.policy_rule_check_result import PolicyRuleCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleCheckResult from a JSON string
policy_rule_check_result_instance = PolicyRuleCheckResult.from_json(json)
# print the JSON string representation of the object
print PolicyRuleCheckResult.to_json()

# convert the object into a dict
policy_rule_check_result_dict = policy_rule_check_result_instance.to_dict()
# create an instance of PolicyRuleCheckResult from a dict
policy_rule_check_result_form_dict = policy_rule_check_result.from_dict(policy_rule_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


