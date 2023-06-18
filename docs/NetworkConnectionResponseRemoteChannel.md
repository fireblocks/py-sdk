# NetworkConnectionResponseRemoteChannel

Deprecated - Replaced by `remoteNetworkId`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.network_connection_response_remote_channel import NetworkConnectionResponseRemoteChannel

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConnectionResponseRemoteChannel from a JSON string
network_connection_response_remote_channel_instance = NetworkConnectionResponseRemoteChannel.from_json(json)
# print the JSON string representation of the object
print NetworkConnectionResponseRemoteChannel.to_json()

# convert the object into a dict
network_connection_response_remote_channel_dict = network_connection_response_remote_channel_instance.to_dict()
# create an instance of NetworkConnectionResponseRemoteChannel from a dict
network_connection_response_remote_channel_form_dict = network_connection_response_remote_channel.from_dict(network_connection_response_remote_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


