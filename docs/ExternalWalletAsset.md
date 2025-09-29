# ExternalWalletAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | [**ConfigChangeRequestStatus**](ConfigChangeRequestStatus.md) |  | [optional] 
**address** | **str** |  | [optional] 
**balance** | **float** |  | [optional] 
**locked_amount** | **float** |  | [optional] 
**tag** | **str** |  | [optional] 
**activation_time** | **str** |  | [optional] 
**additional_info** | [**List[WalletAssetAdditionalInfo]**](WalletAssetAdditionalInfo.md) |  | [optional] 

## Example

```python
from fireblocks.models.external_wallet_asset import ExternalWalletAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalWalletAsset from a JSON string
external_wallet_asset_instance = ExternalWalletAsset.from_json(json)
# print the JSON string representation of the object
print(ExternalWalletAsset.to_json())

# convert the object into a dict
external_wallet_asset_dict = external_wallet_asset_instance.to_dict()
# create an instance of ExternalWalletAsset from a dict
external_wallet_asset_from_dict = ExternalWalletAsset.from_dict(external_wallet_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


