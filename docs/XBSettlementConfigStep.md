# XBSettlementConfigStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_type** | [**XBSettlementStepType**](XBSettlementStepType.md) |  | 
**account_id** | **str** |  | 

## Example

```python
from fireblocks_client.models.xb_settlement_config_step import XBSettlementConfigStep

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementConfigStep from a JSON string
xb_settlement_config_step_instance = XBSettlementConfigStep.from_json(json)
# print the JSON string representation of the object
print XBSettlementConfigStep.to_json()

# convert the object into a dict
xb_settlement_config_step_dict = xb_settlement_config_step_instance.to_dict()
# create an instance of XBSettlementConfigStep from a dict
xb_settlement_config_step_form_dict = xb_settlement_config_step.from_dict(xb_settlement_config_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


