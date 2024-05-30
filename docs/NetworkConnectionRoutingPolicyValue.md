# NetworkConnectionRoutingPolicyValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheme** | **str** | No network routing logic. | 
**dst_type** | **str** | The account the funds are being sent to. | 
**dst_id** | **str** | The ID of the account the funds are being sent to. | 

## Example

```python
from fireblocks.models.network_connection_routing_policy_value import NetworkConnectionRoutingPolicyValue

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConnectionRoutingPolicyValue from a JSON string
network_connection_routing_policy_value_instance = NetworkConnectionRoutingPolicyValue.from_json(json)
# print the JSON string representation of the object
print(NetworkConnectionRoutingPolicyValue.to_json())

# convert the object into a dict
network_connection_routing_policy_value_dict = network_connection_routing_policy_value_instance.to_dict()
# create an instance of NetworkConnectionRoutingPolicyValue from a dict
network_connection_routing_policy_value_from_dict = NetworkConnectionRoutingPolicyValue.from_dict(network_connection_routing_policy_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


