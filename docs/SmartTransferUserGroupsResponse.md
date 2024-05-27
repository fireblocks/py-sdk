# SmartTransferUserGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message | 
**data** | [**SmartTransferUserGroups**](SmartTransferUserGroups.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.smart_transfer_user_groups_response import SmartTransferUserGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferUserGroupsResponse from a JSON string
smart_transfer_user_groups_response_instance = SmartTransferUserGroupsResponse.from_json(json)
# print the JSON string representation of the object
print SmartTransferUserGroupsResponse.to_json()

# convert the object into a dict
smart_transfer_user_groups_response_dict = smart_transfer_user_groups_response_instance.to_dict()
# create an instance of SmartTransferUserGroupsResponse from a dict
smart_transfer_user_groups_response_form_dict = smart_transfer_user_groups_response.from_dict(smart_transfer_user_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


