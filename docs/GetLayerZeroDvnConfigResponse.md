# GetLayerZeroDvnConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_adapter_token_link_id** | **str** | Token-link ID of the adapter for which DVN configuration was queried. | 
**channel_configs** | [**List[ChannelDvnConfigWithConfirmations]**](ChannelDvnConfigWithConfirmations.md) | DVN configurations for each discovered (or explicitly requested) channel between the source adapter and its peers. | 

## Example

```python
from fireblocks.models.get_layer_zero_dvn_config_response import GetLayerZeroDvnConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLayerZeroDvnConfigResponse from a JSON string
get_layer_zero_dvn_config_response_instance = GetLayerZeroDvnConfigResponse.from_json(json)
# print the JSON string representation of the object
print(GetLayerZeroDvnConfigResponse.to_json())

# convert the object into a dict
get_layer_zero_dvn_config_response_dict = get_layer_zero_dvn_config_response_instance.to_dict()
# create an instance of GetLayerZeroDvnConfigResponse from a dict
get_layer_zero_dvn_config_response_from_dict = GetLayerZeroDvnConfigResponse.from_dict(get_layer_zero_dvn_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


