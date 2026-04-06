# AddressRegistryGetVaultOptOutResponse

Whether the given vault account is excluded from the address registry for your workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opted_out** | **bool** | &#x60;true&#x60; if this vault account is excluded from the address registry; &#x60;false&#x60; if it is not excluded.  | 

## Example

```python
from fireblocks.models.address_registry_get_vault_opt_out_response import AddressRegistryGetVaultOptOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryGetVaultOptOutResponse from a JSON string
address_registry_get_vault_opt_out_response_instance = AddressRegistryGetVaultOptOutResponse.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryGetVaultOptOutResponse.to_json())

# convert the object into a dict
address_registry_get_vault_opt_out_response_dict = address_registry_get_vault_opt_out_response_instance.to_dict()
# create an instance of AddressRegistryGetVaultOptOutResponse from a dict
address_registry_get_vault_opt_out_response_from_dict = AddressRegistryGetVaultOptOutResponse.from_dict(address_registry_get_vault_opt_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


