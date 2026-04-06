# AddressRegistryTenantRegistryResponse

Workspace participation in the address registry. Same shape for GET, POST (opt in), and DELETE (opt out).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | OPTED_IN or OPTED_OUT. | 

## Example

```python
from fireblocks.models.address_registry_tenant_registry_response import AddressRegistryTenantRegistryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryTenantRegistryResponse from a JSON string
address_registry_tenant_registry_response_instance = AddressRegistryTenantRegistryResponse.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryTenantRegistryResponse.to_json())

# convert the object into a dict
address_registry_tenant_registry_response_dict = address_registry_tenant_registry_response_instance.to_dict()
# create an instance of AddressRegistryTenantRegistryResponse from a dict
address_registry_tenant_registry_response_from_dict = AddressRegistryTenantRegistryResponse.from_dict(address_registry_tenant_registry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


