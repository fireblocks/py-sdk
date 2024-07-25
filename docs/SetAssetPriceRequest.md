# SetAssetPriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency (according to ISO 4217 currency codes) | 
**price** | **float** | Price in currency | 

## Example

```python
from fireblocks.models.set_asset_price_request import SetAssetPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAssetPriceRequest from a JSON string
set_asset_price_request_instance = SetAssetPriceRequest.from_json(json)
# print the JSON string representation of the object
print(SetAssetPriceRequest.to_json())

# convert the object into a dict
set_asset_price_request_dict = set_asset_price_request_instance.to_dict()
# create an instance of SetAssetPriceRequest from a dict
set_asset_price_request_from_dict = SetAssetPriceRequest.from_dict(set_asset_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


