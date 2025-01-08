# AssetMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Media URL | 
**type** | **str** | Media type | 
**attributes** | [**AssetMediaAttributes**](AssetMediaAttributes.md) |  | [optional] 

## Example

```python
from fireblocks.models.asset_media import AssetMedia

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMedia from a JSON string
asset_media_instance = AssetMedia.from_json(json)
# print the JSON string representation of the object
print(AssetMedia.to_json())

# convert the object into a dict
asset_media_dict = asset_media_instance.to_dict()
# create an instance of AssetMedia from a dict
asset_media_from_dict = AssetMedia.from_dict(asset_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


