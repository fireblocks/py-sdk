# XBSettlementConfigStepsRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_type** | [**XBSettlementStepType**](XBSettlementStepType.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.xb_settlement_config_steps_record import XBSettlementConfigStepsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementConfigStepsRecord from a JSON string
xb_settlement_config_steps_record_instance = XBSettlementConfigStepsRecord.from_json(json)
# print the JSON string representation of the object
print XBSettlementConfigStepsRecord.to_json()

# convert the object into a dict
xb_settlement_config_steps_record_dict = xb_settlement_config_steps_record_instance.to_dict()
# create an instance of XBSettlementConfigStepsRecord from a dict
xb_settlement_config_steps_record_form_dict = xb_settlement_config_steps_record.from_dict(xb_settlement_config_steps_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


