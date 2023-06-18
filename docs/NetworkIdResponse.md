# NetworkIdResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**routing_policy** | [**NetworkIdRoutingPolicy**](NetworkIdRoutingPolicy.md) |  | [optional] 
**is_discoverable** | **bool** | The specific network is discoverable. | [optional] 

## Example

```python
from fireblocks_client.models.network_id_response import NetworkIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkIdResponse from a JSON string
network_id_response_instance = NetworkIdResponse.from_json(json)
# print the JSON string representation of the object
print NetworkIdResponse.to_json()

# convert the object into a dict
network_id_response_dict = network_id_response_instance.to_dict()
# create an instance of NetworkIdResponse from a dict
network_id_response_form_dict = network_id_response.from_dict(network_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


