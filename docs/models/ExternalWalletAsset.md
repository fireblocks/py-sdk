# fireblocks_client.model.external_wallet_asset.ExternalWalletAsset

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**status** | [**ConfigChangeRequestStatus**](ConfigChangeRequestStatus.md) | [**ConfigChangeRequestStatus**](ConfigChangeRequestStatus.md) |  | [optional] 
**address** | str,  | str,  |  | [optional] 
**tag** | str,  | str,  |  | [optional] 
**activationTime** | str,  | str,  |  | [optional] 
**[additionalInfo](#additionalInfo)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# additionalInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WalletAssetAdditionalInfo**](WalletAssetAdditionalInfo.md) | [**WalletAssetAdditionalInfo**](WalletAssetAdditionalInfo.md) | [**WalletAssetAdditionalInfo**](WalletAssetAdditionalInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

