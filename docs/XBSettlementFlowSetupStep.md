# XBSettlementFlowSetupStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**input_amount** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**output_amount** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**estimated_fee_amount** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**estimated_time** | **float** | The estimated time for executing the step. | 
**is_sign_required** | **bool** | Whether or not signing is required for executing the step. | 

## Example

```python
from fireblocks_client.models.xb_settlement_flow_setup_step import XBSettlementFlowSetupStep

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementFlowSetupStep from a JSON string
xb_settlement_flow_setup_step_instance = XBSettlementFlowSetupStep.from_json(json)
# print the JSON string representation of the object
print XBSettlementFlowSetupStep.to_json()

# convert the object into a dict
xb_settlement_flow_setup_step_dict = xb_settlement_flow_setup_step_instance.to_dict()
# create an instance of XBSettlementFlowSetupStep from a dict
xb_settlement_flow_setup_step_form_dict = xb_settlement_flow_setup_step.from_dict(xb_settlement_flow_setup_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


