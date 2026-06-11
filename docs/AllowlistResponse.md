# AllowlistResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AllowlistEntry]**](AllowlistEntry.md) | Array of allowlist entries | 
**metadata** | [**AllowlistMetadata**](AllowlistMetadata.md) |  | [optional] 
**total** | **int** | Total number of allowlist entries | 
**next** | **str** | Cursor for the next page of results, if available | [optional] 

## Example

```python
from fireblocks.models.allowlist_response import AllowlistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllowlistResponse from a JSON string
allowlist_response_instance = AllowlistResponse.from_json(json)
# print the JSON string representation of the object
print(AllowlistResponse.to_json())

# convert the object into a dict
allowlist_response_dict = allowlist_response_instance.to_dict()
# create an instance of AllowlistResponse from a dict
allowlist_response_from_dict = AllowlistResponse.from_dict(allowlist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


