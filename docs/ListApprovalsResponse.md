# ListApprovalsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApprovalRequestItem]**](ApprovalRequestItem.md) | The approval requests the authenticated user is eligible to act on. | 
**next** | **str** | Cursor for the next page of results. Pass it back as the &#x60;pageCursor&#x60; query param to fetch the next page. Empty or absent when this is the last page. | [optional] 

## Example

```python
from fireblocks.models.list_approvals_response import ListApprovalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListApprovalsResponse from a JSON string
list_approvals_response_instance = ListApprovalsResponse.from_json(json)
# print the JSON string representation of the object
print(ListApprovalsResponse.to_json())

# convert the object into a dict
list_approvals_response_dict = list_approvals_response_instance.to_dict()
# create an instance of ListApprovalsResponse from a dict
list_approvals_response_from_dict = ListApprovalsResponse.from_dict(list_approvals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


