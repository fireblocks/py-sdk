# NetworkConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**local_channel** | [**NetworkChannel**](NetworkChannel.md) | Deprecated - Replaced by &#x60;localNetworkId&#x60; | [optional] 
**remote_channel** | [**NetworkChannel**](NetworkChannel.md) | Deprecated - Replaced by &#x60;remoteNetworkId&#x60; | [optional] 
**status** | [**NetworkConnectionStatus**](NetworkConnectionStatus.md) |  | 
**local_network_id** | [**NetworkId**](NetworkId.md) |  | 
**remote_network_id** | [**NetworkId**](NetworkId.md) |  | 
**routing_policy** | [**Dict[str, NetworkConnectionRoutingPolicyValue]**](NetworkConnectionRoutingPolicyValue.md) |  | 

## Example

```python
from fireblocks_client.models.network_connection_response import NetworkConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConnectionResponse from a JSON string
network_connection_response_instance = NetworkConnectionResponse.from_json(json)
# print the JSON string representation of the object
print NetworkConnectionResponse.to_json()

# convert the object into a dict
network_connection_response_dict = network_connection_response_instance.to_dict()
# create an instance of NetworkConnectionResponse from a dict
network_connection_response_form_dict = network_connection_response.from_dict(network_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


