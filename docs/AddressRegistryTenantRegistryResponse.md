# AddressRegistryTenantRegistryResponse

Whether this workspace uses the address registry. GET, POST (opt in), and DELETE (opt out) all return this object. On GET, if this workspace has no explicit choice, `status` follows the customer default when one is set, otherwise the workspace is opted in by default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | &#x60;OPTED_IN&#x60; or &#x60;OPTED_OUT&#x60;. On GET, uses the customer default when this workspace has no setting of its own and the customer has made an explicit choice; is &#x60;OPTED_IN&#x60; when neither is set. On POST or DELETE, reflects the choice you just made for this workspace. | 

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


