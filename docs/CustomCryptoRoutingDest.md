# CustomCryptoRoutingDest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheme** | **str** | The network routing logic. | 
**dst_type** | **str** | The type of destination account the funds are being sent to. | 
**dst_id** | **str** | The ID of the destination account the funds are being sent to. | 

## Example

```python
from fireblocks_client.models.custom_crypto_routing_dest import CustomCryptoRoutingDest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCryptoRoutingDest from a JSON string
custom_crypto_routing_dest_instance = CustomCryptoRoutingDest.from_json(json)
# print the JSON string representation of the object
print CustomCryptoRoutingDest.to_json()

# convert the object into a dict
custom_crypto_routing_dest_dict = custom_crypto_routing_dest_instance.to_dict()
# create an instance of CustomCryptoRoutingDest from a dict
custom_crypto_routing_dest_form_dict = custom_crypto_routing_dest.from_dict(custom_crypto_routing_dest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


