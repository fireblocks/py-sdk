# NetworkConnectionRoutingPolicySignetTest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheme** | **str** | The network routing logic. | 
**dst_type** | **str** | The fiat account the funds are being sent to. | 
**dst_id** | **str** | The ID of the fiat account the funds are being sent to. | 

## Example

```python
from fireblocks_client.models.network_connection_routing_policy_signet_test import NetworkConnectionRoutingPolicySignetTest

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConnectionRoutingPolicySignetTest from a JSON string
network_connection_routing_policy_signet_test_instance = NetworkConnectionRoutingPolicySignetTest.from_json(json)
# print the JSON string representation of the object
print NetworkConnectionRoutingPolicySignetTest.to_json()

# convert the object into a dict
network_connection_routing_policy_signet_test_dict = network_connection_routing_policy_signet_test_instance.to_dict()
# create an instance of NetworkConnectionRoutingPolicySignetTest from a dict
network_connection_routing_policy_signet_test_form_dict = network_connection_routing_policy_signet_test.from_dict(network_connection_routing_policy_signet_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


