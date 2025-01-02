# AssetMetadataBeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the asset | 
**deprecated** | **bool** | Is asset deprecated | 
**deprecation_referral_id** | **str** | New asset ID replacement | [optional] 
**verified** | **bool** | Is asset verified by Fireblocks | 
**website** | **str** | Vendor’s website | [optional] 
**media** | [**List[AssetMedia]**](AssetMedia.md) | Asset’s media | [optional] 

## Example

```python
from fireblocks.models.asset_metadata_beta import AssetMetadataBeta

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMetadataBeta from a JSON string
asset_metadata_beta_instance = AssetMetadataBeta.from_json(json)
# print the JSON string representation of the object
print(AssetMetadataBeta.to_json())

# convert the object into a dict
asset_metadata_beta_dict = asset_metadata_beta_instance.to_dict()
# create an instance of AssetMetadataBeta from a dict
asset_metadata_beta_from_dict = AssetMetadataBeta.from_dict(asset_metadata_beta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


