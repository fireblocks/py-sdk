# XBSettlementFlowExecutionModelSelectedConversionSlippage

Indicates the selected slippage used during the flow since override logic may have taken place.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basis_points** | **float** |  | 
**reason** | [**XBSettlementFlowSelectedConversionSlippageReason**](XBSettlementFlowSelectedConversionSlippageReason.md) |  | 

## Example

```python
from fireblocks_client.models.xb_settlement_flow_execution_model_selected_conversion_slippage import XBSettlementFlowExecutionModelSelectedConversionSlippage

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementFlowExecutionModelSelectedConversionSlippage from a JSON string
xb_settlement_flow_execution_model_selected_conversion_slippage_instance = XBSettlementFlowExecutionModelSelectedConversionSlippage.from_json(json)
# print the JSON string representation of the object
print XBSettlementFlowExecutionModelSelectedConversionSlippage.to_json()

# convert the object into a dict
xb_settlement_flow_execution_model_selected_conversion_slippage_dict = xb_settlement_flow_execution_model_selected_conversion_slippage_instance.to_dict()
# create an instance of XBSettlementFlowExecutionModelSelectedConversionSlippage from a dict
xb_settlement_flow_execution_model_selected_conversion_slippage_form_dict = xb_settlement_flow_execution_model_selected_conversion_slippage.from_dict(xb_settlement_flow_execution_model_selected_conversion_slippage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


