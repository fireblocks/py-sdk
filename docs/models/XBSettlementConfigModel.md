# fireblocks_client.model.xb_settlement_config_model.XBSettlementConfigModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdAt** | decimal.Decimal, int, float,  | decimal.Decimal,  | The creation time in epoch format. | 
**corridorId** | [**XBSettlementCorridorId**](XBSettlementCorridorId.md) | [**XBSettlementCorridorId**](XBSettlementCorridorId.md) |  | 
**configId** | str, uuid.UUID,  | str,  | Cross Bodrder configuraion unique id | value must be a uuid
**conversionSlippageBasisPoints** | [**XBSettlementConversionSlippageBasisPoints**](XBSettlementConversionSlippageBasisPoints.md) | [**XBSettlementConversionSlippageBasisPoints**](XBSettlementConversionSlippageBasisPoints.md) |  | 
**name** | str,  | str,  | The name for the cross-border ettlement configuration | 
**steps** | [**XBSettlementConfigStepsRecord**](XBSettlementConfigStepsRecord.md) | [**XBSettlementConfigStepsRecord**](XBSettlementConfigStepsRecord.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

