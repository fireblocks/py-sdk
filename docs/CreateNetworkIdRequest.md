# CreateNetworkIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**routing_policy** | [**Dict[str, NetworkIdRoutingPolicyValue]**](NetworkIdRoutingPolicyValue.md) |  | [optional] 

## Example

```python
from fireblocks.models.create_network_id_request import CreateNetworkIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNetworkIdRequest from a JSON string
create_network_id_request_instance = CreateNetworkIdRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNetworkIdRequest.to_json())

# convert the object into a dict
create_network_id_request_dict = create_network_id_request_instance.to_dict()
# create an instance of CreateNetworkIdRequest from a dict
create_network_id_request_from_dict = CreateNetworkIdRequest.from_dict(create_network_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


