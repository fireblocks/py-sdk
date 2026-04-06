# AddressRegistryVaultOptOutItem

A vault account excluded from the address registry for your workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **int** | Vault account ID. | 

## Example

```python
from fireblocks.models.address_registry_vault_opt_out_item import AddressRegistryVaultOptOutItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryVaultOptOutItem from a JSON string
address_registry_vault_opt_out_item_instance = AddressRegistryVaultOptOutItem.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryVaultOptOutItem.to_json())

# convert the object into a dict
address_registry_vault_opt_out_item_dict = address_registry_vault_opt_out_item_instance.to_dict()
# create an instance of AddressRegistryVaultOptOutItem from a dict
address_registry_vault_opt_out_item_from_dict = AddressRegistryVaultOptOutItem.from_dict(address_registry_vault_opt_out_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


