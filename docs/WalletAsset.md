# WalletAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**balance** | **str** |  | [optional] 
**locked_amount** | **str** |  | [optional] 
**status** | [**ConfigChangeRequestStatus**](ConfigChangeRequestStatus.md) |  | [optional] 
**address** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**activation_time** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.wallet_asset import WalletAsset

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAsset from a JSON string
wallet_asset_instance = WalletAsset.from_json(json)
# print the JSON string representation of the object
print WalletAsset.to_json()

# convert the object into a dict
wallet_asset_dict = wallet_asset_instance.to_dict()
# create an instance of WalletAsset from a dict
wallet_asset_form_dict = wallet_asset.from_dict(wallet_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


