# XBSettlementFlowExecutionModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | The unique id for the cross-border flow. | 
**config_id** | **str** | Cross Bodrder configuraion unique id | 
**input_amount** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**output_amount** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**total_fee** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**initiated_at** | **float** | The time the cross-border flow executed in epoch format. | 
**initiated_by** | **str** | The id of the user which launched the flow | 
**state** | [**XBSettlementFlowExecutionStatus**](XBSettlementFlowExecutionStatus.md) |  | 
**steps** | [**XBSettlementFlowStepsExecutionRecord**](XBSettlementFlowStepsExecutionRecord.md) |  | 
**selected_conversion_slippage** | [**XBSettlementFlowExecutionModelSelectedConversionSlippage**](XBSettlementFlowExecutionModelSelectedConversionSlippage.md) |  | 

## Example

```python
from fireblocks_client.models.xb_settlement_flow_execution_model import XBSettlementFlowExecutionModel

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementFlowExecutionModel from a JSON string
xb_settlement_flow_execution_model_instance = XBSettlementFlowExecutionModel.from_json(json)
# print the JSON string representation of the object
print XBSettlementFlowExecutionModel.to_json()

# convert the object into a dict
xb_settlement_flow_execution_model_dict = xb_settlement_flow_execution_model_instance.to_dict()
# create an instance of XBSettlementFlowExecutionModel from a dict
xb_settlement_flow_execution_model_form_dict = xb_settlement_flow_execution_model.from_dict(xb_settlement_flow_execution_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


