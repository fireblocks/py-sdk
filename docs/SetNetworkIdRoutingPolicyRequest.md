# SetNetworkIdRoutingPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_policy** | [**Dict[str, NetworkIdRoutingPolicyValue]**](NetworkIdRoutingPolicyValue.md) |  | 

## Example

```python
from fireblocks_client.models.set_network_id_routing_policy_request import SetNetworkIdRoutingPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetNetworkIdRoutingPolicyRequest from a JSON string
set_network_id_routing_policy_request_instance = SetNetworkIdRoutingPolicyRequest.from_json(json)
# print the JSON string representation of the object
print SetNetworkIdRoutingPolicyRequest.to_json()

# convert the object into a dict
set_network_id_routing_policy_request_dict = set_network_id_routing_policy_request_instance.to_dict()
# create an instance of SetNetworkIdRoutingPolicyRequest from a dict
set_network_id_routing_policy_request_form_dict = set_network_id_routing_policy_request.from_dict(set_network_id_routing_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


