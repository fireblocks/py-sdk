# CustomFiatRoutingDest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheme** | **str** | The network routing logic. | 
**dst_type** | **str** | The fiat account the funds are being sent to. | 
**dst_id** | **str** | The ID of the fiat account the funds are being sent to. | 

## Example

```python
from fireblocks_client.models.custom_fiat_routing_dest import CustomFiatRoutingDest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFiatRoutingDest from a JSON string
custom_fiat_routing_dest_instance = CustomFiatRoutingDest.from_json(json)
# print the JSON string representation of the object
print CustomFiatRoutingDest.to_json()

# convert the object into a dict
custom_fiat_routing_dest_dict = custom_fiat_routing_dest_instance.to_dict()
# create an instance of CustomFiatRoutingDest from a dict
custom_fiat_routing_dest_form_dict = custom_fiat_routing_dest.from_dict(custom_fiat_routing_dest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


