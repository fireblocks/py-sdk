# RegisterApprovalApiKeyResponse

The result of registering an approval API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The server-generated ID of the registered key, used for deletion. | 

## Example

```python
from fireblocks.models.register_approval_api_key_response import RegisterApprovalApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterApprovalApiKeyResponse from a JSON string
register_approval_api_key_response_instance = RegisterApprovalApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print(RegisterApprovalApiKeyResponse.to_json())

# convert the object into a dict
register_approval_api_key_response_dict = register_approval_api_key_response_instance.to_dict()
# create an instance of RegisterApprovalApiKeyResponse from a dict
register_approval_api_key_response_from_dict = RegisterApprovalApiKeyResponse.from_dict(register_approval_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


