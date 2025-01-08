# AssetResponseBeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the asset | 
**legacy_id** | **str** | The Legacy ID of the asset | 
**blockchain_id** | **str** | The ID of the asset&#39;s blockchain | [optional] 
**display_name** | **str** | Asset&#39;s display name | [optional] 
**display_symbol** | **str** | Asset&#39;s display symbol | [optional] 
**asset_class** | [**AssetClassBeta**](AssetClassBeta.md) |  | 
**onchain** | [**AssetOnchainBeta**](AssetOnchainBeta.md) |  | [optional] 
**metadata** | [**AssetMetadataBeta**](AssetMetadataBeta.md) |  | 

## Example

```python
from fireblocks.models.asset_response_beta import AssetResponseBeta

# TODO update the JSON string below
json = "{}"
# create an instance of AssetResponseBeta from a JSON string
asset_response_beta_instance = AssetResponseBeta.from_json(json)
# print the JSON string representation of the object
print(AssetResponseBeta.to_json())

# convert the object into a dict
asset_response_beta_dict = asset_response_beta_instance.to_dict()
# create an instance of AssetResponseBeta from a dict
asset_response_beta_from_dict = AssetResponseBeta.from_dict(asset_response_beta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


