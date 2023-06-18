# CreateConnectionResponseSessionMetadata

Metadata of the Web3 connection (provided by the DApp).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** |  | 
**app_name** | **str** |  | [optional] 
**app_description** | **str** |  | [optional] 
**app_icon** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.create_connection_response_session_metadata import CreateConnectionResponseSessionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectionResponseSessionMetadata from a JSON string
create_connection_response_session_metadata_instance = CreateConnectionResponseSessionMetadata.from_json(json)
# print the JSON string representation of the object
print CreateConnectionResponseSessionMetadata.to_json()

# convert the object into a dict
create_connection_response_session_metadata_dict = create_connection_response_session_metadata_instance.to_dict()
# create an instance of CreateConnectionResponseSessionMetadata from a dict
create_connection_response_session_metadata_form_dict = create_connection_response_session_metadata.from_dict(create_connection_response_session_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


