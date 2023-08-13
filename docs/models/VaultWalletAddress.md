# fireblocks_client.model.vault_wallet_address.VaultWalletAddress

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**assetId** | str,  | str,  |  | [optional] 
**address** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**tag** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**customerRefId** | str,  | str,  |  | [optional] 
**addressFormat** | str,  | str,  |  | [optional] must be one of ["SEGWIT", "LEGACY", ] 
**legacyAddress** | str,  | str,  |  | [optional] 
**enterpriseAddress** | str,  | str,  |  | [optional] 
**bip44AddressIndex** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**userDefined** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

