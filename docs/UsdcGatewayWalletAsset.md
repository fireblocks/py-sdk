# UsdcGatewayWalletAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Fireblocks asset ID | 
**balance** | **str** | Asset balance | 
**chain** | **str** | Blockchain name | 
**network** | **str** | Network name | 

## Example

```python
from fireblocks.models.usdc_gateway_wallet_asset import UsdcGatewayWalletAsset

# TODO update the JSON string below
json = "{}"
# create an instance of UsdcGatewayWalletAsset from a JSON string
usdc_gateway_wallet_asset_instance = UsdcGatewayWalletAsset.from_json(json)
# print the JSON string representation of the object
print(UsdcGatewayWalletAsset.to_json())

# convert the object into a dict
usdc_gateway_wallet_asset_dict = usdc_gateway_wallet_asset_instance.to_dict()
# create an instance of UsdcGatewayWalletAsset from a dict
usdc_gateway_wallet_asset_from_dict = UsdcGatewayWalletAsset.from_dict(usdc_gateway_wallet_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


