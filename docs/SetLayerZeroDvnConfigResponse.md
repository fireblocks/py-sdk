# SetLayerZeroDvnConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txn_ids** | **List[str]** | Transaction IDs submitted to the network | 

## Example

```python
from fireblocks.models.set_layer_zero_dvn_config_response import SetLayerZeroDvnConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetLayerZeroDvnConfigResponse from a JSON string
set_layer_zero_dvn_config_response_instance = SetLayerZeroDvnConfigResponse.from_json(json)
# print the JSON string representation of the object
print(SetLayerZeroDvnConfigResponse.to_json())

# convert the object into a dict
set_layer_zero_dvn_config_response_dict = set_layer_zero_dvn_config_response_instance.to_dict()
# create an instance of SetLayerZeroDvnConfigResponse from a dict
set_layer_zero_dvn_config_response_from_dict = SetLayerZeroDvnConfigResponse.from_dict(set_layer_zero_dvn_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


