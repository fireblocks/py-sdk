# AccessRegistryAddressItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address that was added to the access registry | 
**date_added** | **datetime** | The date when the address was added to the access registry | 

## Example

```python
from fireblocks.models.access_registry_address_item import AccessRegistryAddressItem

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRegistryAddressItem from a JSON string
access_registry_address_item_instance = AccessRegistryAddressItem.from_json(json)
# print the JSON string representation of the object
print(AccessRegistryAddressItem.to_json())

# convert the object into a dict
access_registry_address_item_dict = access_registry_address_item_instance.to_dict()
# create an instance of AccessRegistryAddressItem from a dict
access_registry_address_item_from_dict = AccessRegistryAddressItem.from_dict(access_registry_address_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


