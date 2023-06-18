# XBSettlementFlowStepsExecutionRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_type** | [**XBSettlementStepType**](XBSettlementStepType.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.xb_settlement_flow_steps_execution_record import XBSettlementFlowStepsExecutionRecord

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementFlowStepsExecutionRecord from a JSON string
xb_settlement_flow_steps_execution_record_instance = XBSettlementFlowStepsExecutionRecord.from_json(json)
# print the JSON string representation of the object
print XBSettlementFlowStepsExecutionRecord.to_json()

# convert the object into a dict
xb_settlement_flow_steps_execution_record_dict = xb_settlement_flow_steps_execution_record_instance.to_dict()
# create an instance of XBSettlementFlowStepsExecutionRecord from a dict
xb_settlement_flow_steps_execution_record_form_dict = xb_settlement_flow_steps_execution_record.from_dict(xb_settlement_flow_steps_execution_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


