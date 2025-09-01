# LegacyPolicyCheckResult

Policy rules validation result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **float** | Number of errors | 
**results** | [**List[LegacyPolicyRuleCheckResult]**](LegacyPolicyRuleCheckResult.md) | A set of validation results | 

## Example

```python
from fireblocks.models.legacy_policy_check_result import LegacyPolicyCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyCheckResult from a JSON string
legacy_policy_check_result_instance = LegacyPolicyCheckResult.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyCheckResult.to_json())

# convert the object into a dict
legacy_policy_check_result_dict = legacy_policy_check_result_instance.to_dict()
# create an instance of LegacyPolicyCheckResult from a dict
legacy_policy_check_result_from_dict = LegacyPolicyCheckResult.from_dict(legacy_policy_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


