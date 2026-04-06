# AddressRegistryRemoveVaultOptOutResponse

Body after removing one vault from the opt-out list; same fields as GET for that vault (`optedOut` is false).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opted_out** | **bool** | Always false after a successful remove — the vault is not on the opt-out list. | 

## Example

```python
from fireblocks.models.address_registry_remove_vault_opt_out_response import AddressRegistryRemoveVaultOptOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryRemoveVaultOptOutResponse from a JSON string
address_registry_remove_vault_opt_out_response_instance = AddressRegistryRemoveVaultOptOutResponse.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryRemoveVaultOptOutResponse.to_json())

# convert the object into a dict
address_registry_remove_vault_opt_out_response_dict = address_registry_remove_vault_opt_out_response_instance.to_dict()
# create an instance of AddressRegistryRemoveVaultOptOutResponse from a dict
address_registry_remove_vault_opt_out_response_from_dict = AddressRegistryRemoveVaultOptOutResponse.from_dict(address_registry_remove_vault_opt_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


