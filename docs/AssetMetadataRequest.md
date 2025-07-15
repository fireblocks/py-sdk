# AssetMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | [**AssetNoteRequest**](AssetNoteRequest.md) |  | [optional] 

## Example

```python
from fireblocks.models.asset_metadata_request import AssetMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMetadataRequest from a JSON string
asset_metadata_request_instance = AssetMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(AssetMetadataRequest.to_json())

# convert the object into a dict
asset_metadata_request_dict = asset_metadata_request_instance.to_dict()
# create an instance of AssetMetadataRequest from a dict
asset_metadata_request_from_dict = AssetMetadataRequest.from_dict(asset_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


