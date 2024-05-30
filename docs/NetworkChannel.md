# NetworkChannel

Deprecated in the only used reference - NetworkConnectionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.network_channel import NetworkChannel

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkChannel from a JSON string
network_channel_instance = NetworkChannel.from_json(json)
# print the JSON string representation of the object
print(NetworkChannel.to_json())

# convert the object into a dict
network_channel_dict = network_channel_instance.to_dict()
# create an instance of NetworkChannel from a dict
network_channel_from_dict = NetworkChannel.from_dict(network_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


