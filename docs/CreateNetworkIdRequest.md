# CreateNetworkIdRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**routing_policy** | [**NetworkIdRoutingPolicy**](NetworkIdRoutingPolicy.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.create_network_id_request import CreateNetworkIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNetworkIdRequest from a JSON string
create_network_id_request_instance = CreateNetworkIdRequest.from_json(json)
# print the JSON string representation of the object
print CreateNetworkIdRequest.to_json()

# convert the object into a dict
create_network_id_request_dict = create_network_id_request_instance.to_dict()
# create an instance of CreateNetworkIdRequest from a dict
create_network_id_request_form_dict = create_network_id_request.from_dict(create_network_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


