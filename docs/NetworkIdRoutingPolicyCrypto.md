# NetworkIdRoutingPolicyCrypto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheme** | **str** | No network routing logic. | 
**dst_type** | **str** | The type of destination account the funds are being sent to. | 
**dst_id** | **str** | The ID of the destination account the funds are being sent to. | 

## Example

```python
from fireblocks_client.models.network_id_routing_policy_crypto import NetworkIdRoutingPolicyCrypto

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkIdRoutingPolicyCrypto from a JSON string
network_id_routing_policy_crypto_instance = NetworkIdRoutingPolicyCrypto.from_json(json)
# print the JSON string representation of the object
print NetworkIdRoutingPolicyCrypto.to_json()

# convert the object into a dict
network_id_routing_policy_crypto_dict = network_id_routing_policy_crypto_instance.to_dict()
# create an instance of NetworkIdRoutingPolicyCrypto from a dict
network_id_routing_policy_crypto_form_dict = network_id_routing_policy_crypto.from_dict(network_id_routing_policy_crypto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


