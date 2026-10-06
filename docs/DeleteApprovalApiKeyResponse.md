# DeleteApprovalApiKeyResponse

The result of deleting an approval API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ccr_id_pending_deletion** | **str** | Always returned. An empty string when the key was deleted immediately. Otherwise, the ID of the approval request that must be approved before the key is removed; the key stays active until then. The request appears in &#x60;GET /v1/approvals&#x60;. | 

## Example

```python
from fireblocks.models.delete_approval_api_key_response import DeleteApprovalApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteApprovalApiKeyResponse from a JSON string
delete_approval_api_key_response_instance = DeleteApprovalApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteApprovalApiKeyResponse.to_json())

# convert the object into a dict
delete_approval_api_key_response_dict = delete_approval_api_key_response_instance.to_dict()
# create an instance of DeleteApprovalApiKeyResponse from a dict
delete_approval_api_key_response_from_dict = DeleteApprovalApiKeyResponse.from_dict(delete_approval_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


