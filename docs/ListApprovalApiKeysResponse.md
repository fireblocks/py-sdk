# ListApprovalApiKeysResponse

The approval API keys registered for the API user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApprovalApiKey]**](ApprovalApiKey.md) | The registered approval API keys. | 
**next** | **str** | Cursor for the next page of results. Pass it back as the &#x60;pageCursor&#x60; query param to fetch the next page. Empty or absent when this is the last page. | [optional] 

## Example

```python
from fireblocks.models.list_approval_api_keys_response import ListApprovalApiKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListApprovalApiKeysResponse from a JSON string
list_approval_api_keys_response_instance = ListApprovalApiKeysResponse.from_json(json)
# print the JSON string representation of the object
print(ListApprovalApiKeysResponse.to_json())

# convert the object into a dict
list_approval_api_keys_response_dict = list_approval_api_keys_response_instance.to_dict()
# create an instance of ListApprovalApiKeysResponse from a dict
list_approval_api_keys_response_from_dict = ListApprovalApiKeysResponse.from_dict(list_approval_api_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


