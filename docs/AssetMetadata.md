# AssetMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the asset | 
**deprecated** | **bool** | Is asset deprecated | 

## Example

```python
from fireblocks.models.asset_metadata import AssetMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMetadata from a JSON string
asset_metadata_instance = AssetMetadata.from_json(json)
# print the JSON string representation of the object
print(AssetMetadata.to_json())

# convert the object into a dict
asset_metadata_dict = asset_metadata_instance.to_dict()
# create an instance of AssetMetadata from a dict
asset_metadata_from_dict = AssetMetadata.from_dict(asset_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


