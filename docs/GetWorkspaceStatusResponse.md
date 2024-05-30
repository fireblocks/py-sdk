# GetWorkspaceStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Current workspace status | [optional] 

## Example

```python
from fireblocks_client.models.get_workspace_status_response import GetWorkspaceStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkspaceStatusResponse from a JSON string
get_workspace_status_response_instance = GetWorkspaceStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetWorkspaceStatusResponse.to_json())

# convert the object into a dict
get_workspace_status_response_dict = get_workspace_status_response_instance.to_dict()
# create an instance of GetWorkspaceStatusResponse from a dict
get_workspace_status_response_from_dict = GetWorkspaceStatusResponse.from_dict(get_workspace_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


