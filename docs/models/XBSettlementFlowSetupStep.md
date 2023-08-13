# fireblocks_client.model.xb_settlement_flow_setup_step.XBSettlementFlowSetupStep

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**estimatedTime** | decimal.Decimal, int, float,  | decimal.Decimal,  | The estimated time for executing the step. | 
**accountId** | str,  | str,  |  | 
**estimatedFeeAmount** | [**XBSettlementAsset**](XBSettlementAsset.md) | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**outputAmount** | [**XBSettlementAsset**](XBSettlementAsset.md) | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**inputAmount** | [**XBSettlementAsset**](XBSettlementAsset.md) | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**isSignRequired** | bool,  | BoolClass,  | Whether or not signing is required for executing the step. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

