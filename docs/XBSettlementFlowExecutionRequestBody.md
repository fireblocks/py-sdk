# XBSettlementFlowExecutionRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_slippage_basis_points** | **int** | Slippage configuarion in basis points, the default value is 10%  | [optional] [default to 10000]

## Example

```python
from fireblocks_client.models.xb_settlement_flow_execution_request_body import XBSettlementFlowExecutionRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementFlowExecutionRequestBody from a JSON string
xb_settlement_flow_execution_request_body_instance = XBSettlementFlowExecutionRequestBody.from_json(json)
# print the JSON string representation of the object
print XBSettlementFlowExecutionRequestBody.to_json()

# convert the object into a dict
xb_settlement_flow_execution_request_body_dict = xb_settlement_flow_execution_request_body_instance.to_dict()
# create an instance of XBSettlementFlowExecutionRequestBody from a dict
xb_settlement_flow_execution_request_body_form_dict = xb_settlement_flow_execution_request_body.from_dict(xb_settlement_flow_execution_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


