# PolicyValidation

Policy validation object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Validation status | 
**check_result** | [**PolicyCheckResult**](PolicyCheckResult.md) |  | 

## Example

```python
from fireblocks_client.models.policy_validation import PolicyValidation

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyValidation from a JSON string
policy_validation_instance = PolicyValidation.from_json(json)
# print the JSON string representation of the object
print PolicyValidation.to_json()

# convert the object into a dict
policy_validation_dict = policy_validation_instance.to_dict()
# create an instance of PolicyValidation from a dict
policy_validation_form_dict = policy_validation.from_dict(policy_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


