# TRLinkAssetData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | Asset ticker symbol (e.g., BTC, ETH, USDT) | [optional] 
**network** | **str** | Network identifier from Fireblocks (e.g., ETH, BTC) | 
**ucid** | **float** | CoinMarketCap unique coin ID | [optional] 
**contract_address** | **str** | Contract address for tokens | [optional] 
**id** | **str** | Fireblocks asset ID | [optional] 

## Example

```python
from fireblocks.models.tr_link_asset_data import TRLinkAssetData

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkAssetData from a JSON string
tr_link_asset_data_instance = TRLinkAssetData.from_json(json)
# print the JSON string representation of the object
print(TRLinkAssetData.to_json())

# convert the object into a dict
tr_link_asset_data_dict = tr_link_asset_data_instance.to_dict()
# create an instance of TRLinkAssetData from a dict
tr_link_asset_data_from_dict = TRLinkAssetData.from_dict(tr_link_asset_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


