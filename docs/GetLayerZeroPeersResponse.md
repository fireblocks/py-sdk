# GetLayerZeroPeersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter_token_link_id** | **str** | The token link id of the adapter | 
**adapter_address** | **str** | The adapter address | 
**peers** | [**List[PeerAdapterInfo]**](PeerAdapterInfo.md) | The peers for the adapter | 

## Example

```python
from fireblocks.models.get_layer_zero_peers_response import GetLayerZeroPeersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLayerZeroPeersResponse from a JSON string
get_layer_zero_peers_response_instance = GetLayerZeroPeersResponse.from_json(json)
# print the JSON string representation of the object
print(GetLayerZeroPeersResponse.to_json())

# convert the object into a dict
get_layer_zero_peers_response_dict = get_layer_zero_peers_response_instance.to_dict()
# create an instance of GetLayerZeroPeersResponse from a dict
get_layer_zero_peers_response_from_dict = GetLayerZeroPeersResponse.from_dict(get_layer_zero_peers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


