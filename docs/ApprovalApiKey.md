# ApprovalApiKey

A registered approval API key for an API user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique key ID, used to delete the key. | 
**name** | **str** | A human-readable label for the key. | 
**created_at** | **str** | Creation time as epoch time in seconds. | 
**last_used_at** | **str** | Last time the key was used to sign, as epoch time in seconds (0 if never used). | 
**approval_api_public_key** | [**ApprovalApiPublicKey**](ApprovalApiPublicKey.md) |  | 
**user_id** | **str** | The ID of the API user who owns this key. | 
**status** | **str** | The state of the key. &#x60;APPROVAL_API_KEY_STATUS_PENDING_REGISTRATION&#x60; - registered but waiting for approval, cannot sign yet. &#x60;APPROVAL_API_KEY_STATUS_ENABLED&#x60; - active. &#x60;APPROVAL_API_KEY_STATUS_PENDING_DELETION&#x60; - removal is waiting for approval, the key stays active until then. &#x60;APPROVAL_API_KEY_STATUS_UNSPECIFIED&#x60; - unknown. | 

## Example

```python
from fireblocks.models.approval_api_key import ApprovalApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalApiKey from a JSON string
approval_api_key_instance = ApprovalApiKey.from_json(json)
# print the JSON string representation of the object
print(ApprovalApiKey.to_json())

# convert the object into a dict
approval_api_key_dict = approval_api_key_instance.to_dict()
# create an instance of ApprovalApiKey from a dict
approval_api_key_from_dict = ApprovalApiKey.from_dict(approval_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


