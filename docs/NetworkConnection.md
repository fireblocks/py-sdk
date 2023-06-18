# NetworkConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_network_id** | **str** | The network ID of the profile trying to create the connection. | 
**remote_network_id** | **str** | The network ID the profile is attempting to connect to. | 
**routing_policy** | [**NetworkConnectionRoutingPolicy**](NetworkConnectionRoutingPolicy.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.network_connection import NetworkConnection

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConnection from a JSON string
network_connection_instance = NetworkConnection.from_json(json)
# print the JSON string representation of the object
print NetworkConnection.to_json()

# convert the object into a dict
network_connection_dict = network_connection_instance.to_dict()
# create an instance of NetworkConnection from a dict
network_connection_form_dict = network_connection.from_dict(network_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


