# AssetMediaAttributes

Media attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monochrome** | **bool** | Monochrome flag | [optional] 

## Example

```python
from fireblocks.models.asset_media_attributes import AssetMediaAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMediaAttributes from a JSON string
asset_media_attributes_instance = AssetMediaAttributes.from_json(json)
# print the JSON string representation of the object
print(AssetMediaAttributes.to_json())

# convert the object into a dict
asset_media_attributes_dict = asset_media_attributes_instance.to_dict()
# create an instance of AssetMediaAttributes from a dict
asset_media_attributes_from_dict = AssetMediaAttributes.from_dict(asset_media_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


