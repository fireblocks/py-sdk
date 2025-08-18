# SetLayerZeroDvnConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | Vault account that pays gas | 
**source_adapter_token_link_id** | **str** | Source adapter TokenLink ID | 
**destination_adapter_token_link_id** | **str** | Destination adapter TokenLink ID | 
**send_config** | [**DvnConfig**](DvnConfig.md) |  | 
**receive_config** | [**DvnConfig**](DvnConfig.md) |  | 

## Example

```python
from fireblocks.models.set_layer_zero_dvn_config_request import SetLayerZeroDvnConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetLayerZeroDvnConfigRequest from a JSON string
set_layer_zero_dvn_config_request_instance = SetLayerZeroDvnConfigRequest.from_json(json)
# print the JSON string representation of the object
print(SetLayerZeroDvnConfigRequest.to_json())

# convert the object into a dict
set_layer_zero_dvn_config_request_dict = set_layer_zero_dvn_config_request_instance.to_dict()
# create an instance of SetLayerZeroDvnConfigRequest from a dict
set_layer_zero_dvn_config_request_from_dict = SetLayerZeroDvnConfigRequest.from_dict(set_layer_zero_dvn_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


