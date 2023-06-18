# XBSettlementConfigCreationRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the cross-border settlement configuration | 
**corridor_id** | [**XBSettlementCorridorId**](XBSettlementCorridorId.md) |  | 
**steps** | [**XBSettlementConfigStepsRecord**](XBSettlementConfigStepsRecord.md) |  | 
**conversion_slippage_basis_points** | **int** | Slippage configuarion in basis points, the default value is 10%  | [optional] [default to 10000]

## Example

```python
from fireblocks_client.models.xb_settlement_config_creation_request_body import XBSettlementConfigCreationRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementConfigCreationRequestBody from a JSON string
xb_settlement_config_creation_request_body_instance = XBSettlementConfigCreationRequestBody.from_json(json)
# print the JSON string representation of the object
print XBSettlementConfigCreationRequestBody.to_json()

# convert the object into a dict
xb_settlement_config_creation_request_body_dict = xb_settlement_config_creation_request_body_instance.to_dict()
# create an instance of XBSettlementConfigCreationRequestBody from a dict
xb_settlement_config_creation_request_body_form_dict = xb_settlement_config_creation_request_body.from_dict(xb_settlement_config_creation_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


