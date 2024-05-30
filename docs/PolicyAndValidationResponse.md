# PolicyAndValidationResponse

Policy validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**PolicyResponse**](PolicyResponse.md) |  | 
**validation** | [**PolicyValidation**](PolicyValidation.md) |  | 

## Example

```python
from fireblocks_client.models.policy_and_validation_response import PolicyAndValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyAndValidationResponse from a JSON string
policy_and_validation_response_instance = PolicyAndValidationResponse.from_json(json)
# print the JSON string representation of the object
print(PolicyAndValidationResponse.to_json())

# convert the object into a dict
policy_and_validation_response_dict = policy_and_validation_response_instance.to_dict()
# create an instance of PolicyAndValidationResponse from a dict
policy_and_validation_response_from_dict = PolicyAndValidationResponse.from_dict(policy_and_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


