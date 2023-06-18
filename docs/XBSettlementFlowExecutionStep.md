# XBSettlementFlowExecutionStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique id for the step execution | 
**account_id** | **str** |  | 
**status** | [**XBSettlementFlowExecutionStepStatus**](XBSettlementFlowExecutionStepStatus.md) |  | 
**input_amount** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**output_amount** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | [optional] 
**fee** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | [optional] 
**started_at** | **float** | The step execution start time in epoch format. | [optional] 
**completed_at** | **float** | The step execution end time in epoch format. | [optional] 
**is_sign_required** | **bool** | Whether or not signing is required for executing the step. | 

## Example

```python
from fireblocks_client.models.xb_settlement_flow_execution_step import XBSettlementFlowExecutionStep

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementFlowExecutionStep from a JSON string
xb_settlement_flow_execution_step_instance = XBSettlementFlowExecutionStep.from_json(json)
# print the JSON string representation of the object
print XBSettlementFlowExecutionStep.to_json()

# convert the object into a dict
xb_settlement_flow_execution_step_dict = xb_settlement_flow_execution_step_instance.to_dict()
# create an instance of XBSettlementFlowExecutionStep from a dict
xb_settlement_flow_execution_step_form_dict = xb_settlement_flow_execution_step.from_dict(xb_settlement_flow_execution_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


