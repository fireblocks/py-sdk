# NetworkIdRoutingPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto** | [**NetworkIdRoutingPolicyCrypto**](NetworkIdRoutingPolicyCrypto.md) |  | [optional] 
**sen** | [**NetworkIdRoutingPolicySen**](NetworkIdRoutingPolicySen.md) |  | [optional] 
**signet** | [**NetworkIdRoutingPolicySen**](NetworkIdRoutingPolicySen.md) |  | [optional] 
**sen_test** | [**NetworkIdRoutingPolicySenTest**](NetworkIdRoutingPolicySenTest.md) |  | [optional] 
**signet_test** | [**NetworkIdRoutingPolicySenTest**](NetworkIdRoutingPolicySenTest.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.network_id_routing_policy import NetworkIdRoutingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkIdRoutingPolicy from a JSON string
network_id_routing_policy_instance = NetworkIdRoutingPolicy.from_json(json)
# print the JSON string representation of the object
print NetworkIdRoutingPolicy.to_json()

# convert the object into a dict
network_id_routing_policy_dict = network_id_routing_policy_instance.to_dict()
# create an instance of NetworkIdRoutingPolicy from a dict
network_id_routing_policy_form_dict = network_id_routing_policy.from_dict(network_id_routing_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


