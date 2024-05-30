# AssetResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the asset | 
**deprecated** | **bool** | Is asset deprecated | 

## Example

```python
from fireblocks.models.asset_response_metadata import AssetResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AssetResponseMetadata from a JSON string
asset_response_metadata_instance = AssetResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(AssetResponseMetadata.to_json())

# convert the object into a dict
asset_response_metadata_dict = asset_response_metadata_instance.to_dict()
# create an instance of AssetResponseMetadata from a dict
asset_response_metadata_from_dict = AssetResponseMetadata.from_dict(asset_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


