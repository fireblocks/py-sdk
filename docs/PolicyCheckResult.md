# PolicyCheckResult

Policy rules validation result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **float** | Number of errors | 
**result** | [**List[PolicyRuleCheckResult]**](PolicyRuleCheckResult.md) | A set of validation results | 

## Example

```python
from fireblocks_client.models.policy_check_result import PolicyCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyCheckResult from a JSON string
policy_check_result_instance = PolicyCheckResult.from_json(json)
# print the JSON string representation of the object
print PolicyCheckResult.to_json()

# convert the object into a dict
policy_check_result_dict = policy_check_result_instance.to_dict()
# create an instance of PolicyCheckResult from a dict
policy_check_result_form_dict = policy_check_result.from_dict(policy_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


