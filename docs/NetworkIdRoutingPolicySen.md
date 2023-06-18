# NetworkIdRoutingPolicySen


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheme** | **str** | No network routing logic. | 
**dst_type** | **str** | The fiat account the funds are being sent to. | 
**dst_id** | **str** | The ID of the fiat account the funds are being sent to. | 

## Example

```python
from fireblocks_client.models.network_id_routing_policy_sen import NetworkIdRoutingPolicySen

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkIdRoutingPolicySen from a JSON string
network_id_routing_policy_sen_instance = NetworkIdRoutingPolicySen.from_json(json)
# print the JSON string representation of the object
print NetworkIdRoutingPolicySen.to_json()

# convert the object into a dict
network_id_routing_policy_sen_dict = network_id_routing_policy_sen_instance.to_dict()
# create an instance of NetworkIdRoutingPolicySen from a dict
network_id_routing_policy_sen_form_dict = network_id_routing_policy_sen.from_dict(network_id_routing_policy_sen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


