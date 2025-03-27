# AssetDetailsMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**AssetScope**](AssetScope.md) |  | 
**deprecated** | **bool** | Is asset deprecated | 
**deprecation_referral_id** | **str** | New asset ID replacement | [optional] 
**website** | **str** | Vendor’s website | [optional] 
**media** | [**List[AssetMedia]**](AssetMedia.md) | Asset’s media | [optional] 

## Example

```python
from fireblocks.models.asset_details_metadata import AssetDetailsMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDetailsMetadata from a JSON string
asset_details_metadata_instance = AssetDetailsMetadata.from_json(json)
# print the JSON string representation of the object
print(AssetDetailsMetadata.to_json())

# convert the object into a dict
asset_details_metadata_dict = asset_details_metadata_instance.to_dict()
# create an instance of AssetDetailsMetadata from a dict
asset_details_metadata_from_dict = AssetDetailsMetadata.from_dict(asset_details_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


