# XBSettlementConfigModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Cross Bodrder configuraion unique id | 
**corridor_id** | [**XBSettlementCorridorId**](XBSettlementCorridorId.md) |  | 
**name** | **str** | The name for the cross-border ettlement configuration | 
**steps** | [**XBSettlementConfigStepsRecord**](XBSettlementConfigStepsRecord.md) |  | 
**conversion_slippage_basis_points** | **int** | Slippage configuarion in basis points, the default value is 10%  | [default to 10000]
**created_at** | **float** | The creation time in epoch format. | 

## Example

```python
from fireblocks_client.models.xb_settlement_config_model import XBSettlementConfigModel

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementConfigModel from a JSON string
xb_settlement_config_model_instance = XBSettlementConfigModel.from_json(json)
# print the JSON string representation of the object
print XBSettlementConfigModel.to_json()

# convert the object into a dict
xb_settlement_config_model_dict = xb_settlement_config_model_instance.to_dict()
# create an instance of XBSettlementConfigModel from a dict
xb_settlement_config_model_form_dict = xb_settlement_config_model.from_dict(xb_settlement_config_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


