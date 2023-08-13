# fireblocks_client.model.xb_settlement_flow_execution_model.XBSettlementFlowExecutionModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**initiatedAt** | decimal.Decimal, int, float,  | decimal.Decimal,  | The time the cross-border flow executed in epoch format. | 
**totalFee** | [**XBSettlementAsset**](XBSettlementAsset.md) | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**configId** | str, uuid.UUID,  | str,  | Cross Bodrder configuraion unique id | value must be a uuid
**outputAmount** | [**XBSettlementAsset**](XBSettlementAsset.md) | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**inputAmount** | [**XBSettlementAsset**](XBSettlementAsset.md) | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**state** | [**XBSettlementFlowExecutionStatus**](XBSettlementFlowExecutionStatus.md) | [**XBSettlementFlowExecutionStatus**](XBSettlementFlowExecutionStatus.md) |  | 
**flowId** | str,  | str,  | The unique id for the cross-border flow. | 
**steps** | [**XBSettlementFlowStepsExecutionRecord**](XBSettlementFlowStepsExecutionRecord.md) | [**XBSettlementFlowStepsExecutionRecord**](XBSettlementFlowStepsExecutionRecord.md) |  | 
**initiatedBy** | str,  | str,  | The id of the user which launched the flow | 
**[selectedConversionSlippage](#selectedConversionSlippage)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Indicates the selected slippage used during the flow since override logic may have taken place. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# selectedConversionSlippage

Indicates the selected slippage used during the flow since override logic may have taken place.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Indicates the selected slippage used during the flow since override logic may have taken place. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reason** | [**XBSettlementFlowSelectedConversionSlippageReason**](XBSettlementFlowSelectedConversionSlippageReason.md) | [**XBSettlementFlowSelectedConversionSlippageReason**](XBSettlementFlowSelectedConversionSlippageReason.md) |  | 
**basisPoints** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

