# CustomRoutingDest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheme** | **str** | The network routing logic. | 
**dst_type** | **str** | The account the funds are being sent to. | 
**dst_id** | **str** | The ID of the account the funds are being sent to. | 

## Example

```python
from fireblocks_client.models.custom_routing_dest import CustomRoutingDest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRoutingDest from a JSON string
custom_routing_dest_instance = CustomRoutingDest.from_json(json)
# print the JSON string representation of the object
print(CustomRoutingDest.to_json())

# convert the object into a dict
custom_routing_dest_dict = custom_routing_dest_instance.to_dict()
# create an instance of CustomRoutingDest from a dict
custom_routing_dest_from_dict = CustomRoutingDest.from_dict(custom_routing_dest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


