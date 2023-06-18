# XBSettlementConfigStepsRecordValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**input_asset_id** | [**XBSettlementAssetID**](XBSettlementAssetID.md) |  | [optional] 
**output_asset_id** | [**XBSettlementAssetID**](XBSettlementAssetID.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.xb_settlement_config_steps_record_value import XBSettlementConfigStepsRecordValue

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementConfigStepsRecordValue from a JSON string
xb_settlement_config_steps_record_value_instance = XBSettlementConfigStepsRecordValue.from_json(json)
# print the JSON string representation of the object
print XBSettlementConfigStepsRecordValue.to_json()

# convert the object into a dict
xb_settlement_config_steps_record_value_dict = xb_settlement_config_steps_record_value_instance.to_dict()
# create an instance of XBSettlementConfigStepsRecordValue from a dict
xb_settlement_config_steps_record_value_form_dict = xb_settlement_config_steps_record_value.from_dict(xb_settlement_config_steps_record_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


