# AddressRegistryRemoveAllVaultOptOutsResponse

Result of clearing all vault-level opt-outs for the address registry on this workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**removed_count** | **int** | Number of opt-out rows deleted (0 if none existed). | 

## Example

```python
from fireblocks.models.address_registry_remove_all_vault_opt_outs_response import AddressRegistryRemoveAllVaultOptOutsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryRemoveAllVaultOptOutsResponse from a JSON string
address_registry_remove_all_vault_opt_outs_response_instance = AddressRegistryRemoveAllVaultOptOutsResponse.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryRemoveAllVaultOptOutsResponse.to_json())

# convert the object into a dict
address_registry_remove_all_vault_opt_outs_response_dict = address_registry_remove_all_vault_opt_outs_response_instance.to_dict()
# create an instance of AddressRegistryRemoveAllVaultOptOutsResponse from a dict
address_registry_remove_all_vault_opt_outs_response_from_dict = AddressRegistryRemoveAllVaultOptOutsResponse.from_dict(address_registry_remove_all_vault_opt_outs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


