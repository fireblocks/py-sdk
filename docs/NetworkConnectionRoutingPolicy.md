# NetworkConnectionRoutingPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto** | [**NetworkConnectionRoutingPolicyCrypto**](NetworkConnectionRoutingPolicyCrypto.md) |  | [optional] 
**sen** | [**NetworkConnectionRoutingPolicySen**](NetworkConnectionRoutingPolicySen.md) |  | [optional] 
**signet** | [**NetworkConnectionRoutingPolicySignet**](NetworkConnectionRoutingPolicySignet.md) |  | [optional] 
**sen_test** | [**NetworkConnectionRoutingPolicySenTest**](NetworkConnectionRoutingPolicySenTest.md) |  | [optional] 
**signet_test** | [**NetworkConnectionRoutingPolicySignetTest**](NetworkConnectionRoutingPolicySignetTest.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.network_connection_routing_policy import NetworkConnectionRoutingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConnectionRoutingPolicy from a JSON string
network_connection_routing_policy_instance = NetworkConnectionRoutingPolicy.from_json(json)
# print the JSON string representation of the object
print NetworkConnectionRoutingPolicy.to_json()

# convert the object into a dict
network_connection_routing_policy_dict = network_connection_routing_policy_instance.to_dict()
# create an instance of NetworkConnectionRoutingPolicy from a dict
network_connection_routing_policy_form_dict = network_connection_routing_policy.from_dict(network_connection_routing_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


