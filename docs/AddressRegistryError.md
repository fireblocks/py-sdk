# AddressRegistryError

Error body for address-registry 4xx and 5xx.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Numeric error code (2140–2143) for 403, 404 and 5xx responses. | [optional] 
**message** | **str** | Human-readable error message | 

## Example

```python
from fireblocks.models.address_registry_error import AddressRegistryError

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryError from a JSON string
address_registry_error_instance = AddressRegistryError.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryError.to_json())

# convert the object into a dict
address_registry_error_dict = address_registry_error_instance.to_dict()
# create an instance of AddressRegistryError from a dict
address_registry_error_from_dict = AddressRegistryError.from_dict(address_registry_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


