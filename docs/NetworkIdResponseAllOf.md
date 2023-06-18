# NetworkIdResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_policy** | [**NetworkIdRoutingPolicy**](NetworkIdRoutingPolicy.md) |  | [optional] 
**is_discoverable** | **bool** | The specific network is discoverable. | [optional] 

## Example

```python
from fireblocks_client.models.network_id_response_all_of import NetworkIdResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkIdResponseAllOf from a JSON string
network_id_response_all_of_instance = NetworkIdResponseAllOf.from_json(json)
# print the JSON string representation of the object
print NetworkIdResponseAllOf.to_json()

# convert the object into a dict
network_id_response_all_of_dict = network_id_response_all_of_instance.to_dict()
# create an instance of NetworkIdResponseAllOf from a dict
network_id_response_all_of_form_dict = network_id_response_all_of.from_dict(network_id_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


