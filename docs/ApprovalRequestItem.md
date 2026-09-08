# ApprovalRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_payload** | **str** | The pending approval request as a JSON string, exactly as produced by the backend — this is the precise string to sign in order to approve the request (sign it as-is; do not re-serialize). The JSON has the shape { requestId, requestType, requestTimestamp (epoch ms), expiresAt (epoch seconds), requestData }, where requestData is the request-type-specific payload. | 
**request_signature** | **str** | Signature over the requestPayload. Empty until request signing is implemented. | [optional] 
**user_status** | **str** | The authenticated user&#39;s approval status for this request. | 
**quorum_status** | [**QuorumStatus**](QuorumStatus.md) |  | [optional] 

## Example

```python
from fireblocks.models.approval_request_item import ApprovalRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRequestItem from a JSON string
approval_request_item_instance = ApprovalRequestItem.from_json(json)
# print the JSON string representation of the object
print(ApprovalRequestItem.to_json())

# convert the object into a dict
approval_request_item_dict = approval_request_item_instance.to_dict()
# create an instance of ApprovalRequestItem from a dict
approval_request_item_from_dict = ApprovalRequestItem.from_dict(approval_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


