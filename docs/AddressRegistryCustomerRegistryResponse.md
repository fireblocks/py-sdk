# AddressRegistryCustomerRegistryResponse

Your customer's organization-wide address registry default. Workspaces without their own setting use this value. GET, POST (opt in), and DELETE (opt out) all return this object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | &#x60;NOT_SET&#x60;, &#x60;OPTED_IN&#x60;, or &#x60;OPTED_OUT&#x60;. On GET, &#x60;NOT_SET&#x60; means no default has been chosen yet. On POST or DELETE, returns &#x60;OPTED_IN&#x60; or &#x60;OPTED_OUT&#x60; after a successful change. | 

## Example

```python
from fireblocks.models.address_registry_customer_registry_response import AddressRegistryCustomerRegistryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryCustomerRegistryResponse from a JSON string
address_registry_customer_registry_response_instance = AddressRegistryCustomerRegistryResponse.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryCustomerRegistryResponse.to_json())

# convert the object into a dict
address_registry_customer_registry_response_dict = address_registry_customer_registry_response_instance.to_dict()
# create an instance of AddressRegistryCustomerRegistryResponse from a dict
address_registry_customer_registry_response_from_dict = AddressRegistryCustomerRegistryResponse.from_dict(address_registry_customer_registry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


