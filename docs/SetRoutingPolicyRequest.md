# SetRoutingPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_policy** | [**Dict[str, NetworkConnectionRoutingPolicyValue]**](NetworkConnectionRoutingPolicyValue.md) |  | 

## Example

```python
from fireblocks.models.set_routing_policy_request import SetRoutingPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetRoutingPolicyRequest from a JSON string
set_routing_policy_request_instance = SetRoutingPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(SetRoutingPolicyRequest.to_json())

# convert the object into a dict
set_routing_policy_request_dict = set_routing_policy_request_instance.to_dict()
# create an instance of SetRoutingPolicyRequest from a dict
set_routing_policy_request_from_dict = SetRoutingPolicyRequest.from_dict(set_routing_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


