# XBSettlementFlowPreviewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | The unique id for the cross-border flow. | 
**config_id** | **str** | Cross Bodrder configuraion unique id | 
**conversion_rate** | **str** | The conversion rate received from the on-ramp or off-ramp. | 
**input_amount** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**estimated_output_amount** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**total_estimated_fee** | [**XBSettlementAsset**](XBSettlementAsset.md) |  | 
**total_estimated_time** | **float** | The total *estimated* time for executing the cross-border flow. | 
**steps** | [**XBSettlementFlowStepsRecord**](XBSettlementFlowStepsRecord.md) |  | 

## Example

```python
from fireblocks_client.models.xb_settlement_flow_preview_model import XBSettlementFlowPreviewModel

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementFlowPreviewModel from a JSON string
xb_settlement_flow_preview_model_instance = XBSettlementFlowPreviewModel.from_json(json)
# print the JSON string representation of the object
print XBSettlementFlowPreviewModel.to_json()

# convert the object into a dict
xb_settlement_flow_preview_model_dict = xb_settlement_flow_preview_model_instance.to_dict()
# create an instance of XBSettlementFlowPreviewModel from a dict
xb_settlement_flow_preview_model_form_dict = xb_settlement_flow_preview_model.from_dict(xb_settlement_flow_preview_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


