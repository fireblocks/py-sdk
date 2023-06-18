# XBSettlementCreateFlowRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Cross Bodrder configuraion unique id | 
**amount** | **str** | The amount to transfer in this cross-border flow. The type of asset is defined by the cross-border settlement configuration. | 

## Example

```python
from fireblocks_client.models.xb_settlement_create_flow_request_body import XBSettlementCreateFlowRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementCreateFlowRequestBody from a JSON string
xb_settlement_create_flow_request_body_instance = XBSettlementCreateFlowRequestBody.from_json(json)
# print the JSON string representation of the object
print XBSettlementCreateFlowRequestBody.to_json()

# convert the object into a dict
xb_settlement_create_flow_request_body_dict = xb_settlement_create_flow_request_body_instance.to_dict()
# create an instance of XBSettlementCreateFlowRequestBody from a dict
xb_settlement_create_flow_request_body_form_dict = xb_settlement_create_flow_request_body.from_dict(xb_settlement_create_flow_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


