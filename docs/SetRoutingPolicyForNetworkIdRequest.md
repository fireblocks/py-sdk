# SetRoutingPolicyForNetworkIdRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_policy** | [**NetworkIdRoutingPolicy**](NetworkIdRoutingPolicy.md) |  | 

## Example

```python
from fireblocks_client.models.set_routing_policy_for_network_id_request import SetRoutingPolicyForNetworkIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetRoutingPolicyForNetworkIdRequest from a JSON string
set_routing_policy_for_network_id_request_instance = SetRoutingPolicyForNetworkIdRequest.from_json(json)
# print the JSON string representation of the object
print SetRoutingPolicyForNetworkIdRequest.to_json()

# convert the object into a dict
set_routing_policy_for_network_id_request_dict = set_routing_policy_for_network_id_request_instance.to_dict()
# create an instance of SetRoutingPolicyForNetworkIdRequest from a dict
set_routing_policy_for_network_id_request_form_dict = set_routing_policy_for_network_id_request.from_dict(set_routing_policy_for_network_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


