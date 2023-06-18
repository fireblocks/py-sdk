# XBSettlementGetFlowResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview** | [**XBSettlementFlowPreviewModel**](XBSettlementFlowPreviewModel.md) |  | [optional] 
**execution** | [**XBSettlementFlowExecutionModel**](XBSettlementFlowExecutionModel.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.xb_settlement_get_flow_response import XBSettlementGetFlowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementGetFlowResponse from a JSON string
xb_settlement_get_flow_response_instance = XBSettlementGetFlowResponse.from_json(json)
# print the JSON string representation of the object
print XBSettlementGetFlowResponse.to_json()

# convert the object into a dict
xb_settlement_get_flow_response_dict = xb_settlement_get_flow_response_instance.to_dict()
# create an instance of XBSettlementGetFlowResponse from a dict
xb_settlement_get_flow_response_form_dict = xb_settlement_get_flow_response.from_dict(xb_settlement_get_flow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


