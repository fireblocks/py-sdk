# LegacyPolicyRuleCheckResult

The rule validation result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** | Rule index number in the policy | 
**status** | **str** | Validation status | 
**errors** | [**List[LegacyPolicyRuleError]**](LegacyPolicyRuleError.md) | A set of rule validation error objects | 

## Example

```python
from fireblocks.models.legacy_policy_rule_check_result import LegacyPolicyRuleCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRuleCheckResult from a JSON string
legacy_policy_rule_check_result_instance = LegacyPolicyRuleCheckResult.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRuleCheckResult.to_json())

# convert the object into a dict
legacy_policy_rule_check_result_dict = legacy_policy_rule_check_result_instance.to_dict()
# create an instance of LegacyPolicyRuleCheckResult from a dict
legacy_policy_rule_check_result_from_dict = LegacyPolicyRuleCheckResult.from_dict(legacy_policy_rule_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


