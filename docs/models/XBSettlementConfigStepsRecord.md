# fireblocks_client.model.xb_settlement_config_steps_record.XBSettlementConfigStepsRecord

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**stepType** | [**XBSettlementStepType**](XBSettlementStepType.md) | [**XBSettlementStepType**](XBSettlementStepType.md) |  | [optional] 
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accountId** | str,  | str,  |  | 
**inputAssetId** | [**XBSettlementAssetID**](XBSettlementAssetID.md) | [**XBSettlementAssetID**](XBSettlementAssetID.md) |  | [optional] 
**outputAssetId** | [**XBSettlementAssetID**](XBSettlementAssetID.md) | [**XBSettlementAssetID**](XBSettlementAssetID.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

