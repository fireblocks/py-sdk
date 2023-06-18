# SetRoutingPolicyForNetworkConnectionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_policy** | [**NetworkConnectionRoutingPolicy**](NetworkConnectionRoutingPolicy.md) |  | 

## Example

```python
from fireblocks_client.models.set_routing_policy_for_network_connection_request import SetRoutingPolicyForNetworkConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetRoutingPolicyForNetworkConnectionRequest from a JSON string
set_routing_policy_for_network_connection_request_instance = SetRoutingPolicyForNetworkConnectionRequest.from_json(json)
# print the JSON string representation of the object
print SetRoutingPolicyForNetworkConnectionRequest.to_json()

# convert the object into a dict
set_routing_policy_for_network_connection_request_dict = set_routing_policy_for_network_connection_request_instance.to_dict()
# create an instance of SetRoutingPolicyForNetworkConnectionRequest from a dict
set_routing_policy_for_network_connection_request_form_dict = set_routing_policy_for_network_connection_request.from_dict(set_routing_policy_for_network_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


