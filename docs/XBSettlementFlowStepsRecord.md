# XBSettlementFlowStepsRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_type** | [**XBSettlementStepType**](XBSettlementStepType.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.xb_settlement_flow_steps_record import XBSettlementFlowStepsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementFlowStepsRecord from a JSON string
xb_settlement_flow_steps_record_instance = XBSettlementFlowStepsRecord.from_json(json)
# print the JSON string representation of the object
print XBSettlementFlowStepsRecord.to_json()

# convert the object into a dict
xb_settlement_flow_steps_record_dict = xb_settlement_flow_steps_record_instance.to_dict()
# create an instance of XBSettlementFlowStepsRecord from a dict
xb_settlement_flow_steps_record_form_dict = xb_settlement_flow_steps_record.from_dict(xb_settlement_flow_steps_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


