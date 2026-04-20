# AddressRegistryError

Error body for address registry operations (4xx and 5xx).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Application error code when present. For HTTP 400 on legal-entity lookup, distinguish: 4100 — request validation (e.g. missing, empty, or whitespace-only &#x60;address&#x60; after trim); 2140 — workspace not opted in to the address registry (&#x60;AR_OPT_IN_REQUIRED&#x60;). 2142 — not found (404). Other codes may appear, including on server errors.  | [optional] 
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


