# fireblocks_client.model.xb_settlement_flow_execution_step.XBSettlementFlowExecutionStep

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accountId** | str,  | str,  |  | 
**inputAmount** | [**XBSettlementAsset**](XBSettlementAsset.md) | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**id** | str,  | str,  | A unique id for the step execution | 
**isSignRequired** | bool,  | BoolClass,  | Whether or not signing is required for executing the step. | 
**status** | [**XBSettlementFlowExecutionStepStatus**](XBSettlementFlowExecutionStepStatus.md) | [**XBSettlementFlowExecutionStepStatus**](XBSettlementFlowExecutionStepStatus.md) |  | 
**outputAmount** | [**XBSettlementAsset**](XBSettlementAsset.md) | [**XBSettlementAsset**](XBSettlementAsset.md) |  | [optional] 
**fee** | [**XBSettlementAsset**](XBSettlementAsset.md) | [**XBSettlementAsset**](XBSettlementAsset.md) |  | [optional] 
**startedAt** | decimal.Decimal, int, float,  | decimal.Decimal,  | The step execution start time in epoch format. | [optional] 
**completedAt** | decimal.Decimal, int, float,  | decimal.Decimal,  | The step execution end time in epoch format. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

