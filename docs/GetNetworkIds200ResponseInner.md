# GetNetworkIds200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**routing_policy** | [**NetworkIdRoutingPolicy**](NetworkIdRoutingPolicy.md) |  | [optional] 
**is_discoverable** | **bool** | The specific network is discoverable. | [optional] 

## Example

```python
from fireblocks_client.models.get_network_ids200_response_inner import GetNetworkIds200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkIds200ResponseInner from a JSON string
get_network_ids200_response_inner_instance = GetNetworkIds200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetNetworkIds200ResponseInner.to_json()

# convert the object into a dict
get_network_ids200_response_inner_dict = get_network_ids200_response_inner_instance.to_dict()
# create an instance of GetNetworkIds200ResponseInner from a dict
get_network_ids200_response_inner_form_dict = get_network_ids200_response_inner.from_dict(get_network_ids200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


