# SessionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** |  | 
**app_name** | **str** |  | [optional] 
**app_description** | **str** |  | [optional] 
**app_icon** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.session_metadata import SessionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SessionMetadata from a JSON string
session_metadata_instance = SessionMetadata.from_json(json)
# print the JSON string representation of the object
print(SessionMetadata.to_json())

# convert the object into a dict
session_metadata_dict = session_metadata_instance.to_dict()
# create an instance of SessionMetadata from a dict
session_metadata_from_dict = SessionMetadata.from_dict(session_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


