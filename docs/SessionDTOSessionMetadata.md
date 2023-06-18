# SessionDTOSessionMetadata

Metadata of the connection (provided by the dapp)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** |  | 
**app_name** | **str** |  | [optional] 
**app_description** | **str** |  | [optional] 
**app_icon** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.session_dto_session_metadata import SessionDTOSessionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SessionDTOSessionMetadata from a JSON string
session_dto_session_metadata_instance = SessionDTOSessionMetadata.from_json(json)
# print the JSON string representation of the object
print SessionDTOSessionMetadata.to_json()

# convert the object into a dict
session_dto_session_metadata_dict = session_dto_session_metadata_instance.to_dict()
# create an instance of SessionDTOSessionMetadata from a dict
session_dto_session_metadata_form_dict = session_dto_session_metadata.from_dict(session_dto_session_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


