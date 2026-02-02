# ApprovalRequest

Approval request details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The approval request identifier | 
**type** | **str** | The approval request type | 
**state** | **str** | The approval request state | 

## Example

```python
from fireblocks.models.approval_request import ApprovalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRequest from a JSON string
approval_request_instance = ApprovalRequest.from_json(json)
# print the JSON string representation of the object
print(ApprovalRequest.to_json())

# convert the object into a dict
approval_request_dict = approval_request_instance.to_dict()
# create an instance of ApprovalRequest from a dict
approval_request_from_dict = ApprovalRequest.from_dict(approval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


