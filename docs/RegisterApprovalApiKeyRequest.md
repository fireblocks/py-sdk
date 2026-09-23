# RegisterApprovalApiKeyRequest

The approval API key to register.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-readable label for the key. | 
**approval_api_public_key** | [**ApprovalApiPublicKey**](ApprovalApiPublicKey.md) |  | 

## Example

```python
from fireblocks.models.register_approval_api_key_request import RegisterApprovalApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterApprovalApiKeyRequest from a JSON string
register_approval_api_key_request_instance = RegisterApprovalApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterApprovalApiKeyRequest.to_json())

# convert the object into a dict
register_approval_api_key_request_dict = register_approval_api_key_request_instance.to_dict()
# create an instance of RegisterApprovalApiKeyRequest from a dict
register_approval_api_key_request_from_dict = RegisterApprovalApiKeyRequest.from_dict(register_approval_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


