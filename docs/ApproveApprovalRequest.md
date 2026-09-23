# ApproveApprovalRequest

The signed approval of a pending request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The ID of the approval API key used to sign the request. Optional — if omitted, the signature is verified against all of the user&#39;s registered approval API keys. | [optional] 
**signature** | **str** | Base64url-encoded signature over the request&#39;s signable data, produced with the private key of a registered approval API key. If keyId is provided the signature must match that key; otherwise it is matched against all of the user&#39;s registered keys. | 

## Example

```python
from fireblocks.models.approve_approval_request import ApproveApprovalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveApprovalRequest from a JSON string
approve_approval_request_instance = ApproveApprovalRequest.from_json(json)
# print the JSON string representation of the object
print(ApproveApprovalRequest.to_json())

# convert the object into a dict
approve_approval_request_dict = approve_approval_request_instance.to_dict()
# create an instance of ApproveApprovalRequest from a dict
approve_approval_request_from_dict = ApproveApprovalRequest.from_dict(approve_approval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


