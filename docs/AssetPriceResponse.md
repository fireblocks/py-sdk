# AssetPriceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_id** | **str** | The ID of the asset | 
**last_update_at** | **float** | Time of last price update | 
**currency** | **str** | Currency (according to ISO 4217 currency codes) | 
**price** | **float** | Price in currency | 
**source** | **str** | Source of the price data | 

## Example

```python
from fireblocks.models.asset_price_response import AssetPriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPriceResponse from a JSON string
asset_price_response_instance = AssetPriceResponse.from_json(json)
# print the JSON string representation of the object
print(AssetPriceResponse.to_json())

# convert the object into a dict
asset_price_response_dict = asset_price_response_instance.to_dict()
# create an instance of AssetPriceResponse from a dict
asset_price_response_from_dict = AssetPriceResponse.from_dict(asset_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


