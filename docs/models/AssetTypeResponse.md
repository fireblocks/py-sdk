# fireblocks_client.model.asset_type_response.AssetTypeResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**id** | str,  | str,  |  | 
**type** | str,  | str,  |  | must be one of ["ALGO_ASSET", "BASE_ASSET", "BEP20", "COMPOUND", "ERC20", "FIAT", "SOL_ASSET", "TRON_TRC20", "XLM_ASSET", "XDB_ASSET", ] 
**contractAddress** | str,  | str,  |  | [optional] 
**nativeAsset** | str,  | str,  |  | [optional] 
**decimals** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

