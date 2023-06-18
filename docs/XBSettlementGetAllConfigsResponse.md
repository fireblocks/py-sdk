# XBSettlementGetAllConfigsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurations** | [**List[XBSettlementConfigModel]**](XBSettlementConfigModel.md) |  | 

## Example

```python
from fireblocks_client.models.xb_settlement_get_all_configs_response import XBSettlementGetAllConfigsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementGetAllConfigsResponse from a JSON string
xb_settlement_get_all_configs_response_instance = XBSettlementGetAllConfigsResponse.from_json(json)
# print the JSON string representation of the object
print XBSettlementGetAllConfigsResponse.to_json()

# convert the object into a dict
xb_settlement_get_all_configs_response_dict = xb_settlement_get_all_configs_response_instance.to_dict()
# create an instance of XBSettlementGetAllConfigsResponse from a dict
xb_settlement_get_all_configs_response_form_dict = xb_settlement_get_all_configs_response.from_dict(xb_settlement_get_all_configs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


