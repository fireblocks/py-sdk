# AddressRegistryAddVaultOptOutsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_ids** | [**List[AddressRegistryAddVaultOptOutsRequestVaultAccountIdsInner]**](AddressRegistryAddVaultOptOutsRequestVaultAccountIdsInner.md) | Vault account ids to add to the opt-out list (non-empty). Each element may be a JSON number or a decimal string; both forms are accepted.  | 

## Example

```python
from fireblocks.models.address_registry_add_vault_opt_outs_request import AddressRegistryAddVaultOptOutsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryAddVaultOptOutsRequest from a JSON string
address_registry_add_vault_opt_outs_request_instance = AddressRegistryAddVaultOptOutsRequest.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryAddVaultOptOutsRequest.to_json())

# convert the object into a dict
address_registry_add_vault_opt_outs_request_dict = address_registry_add_vault_opt_outs_request_instance.to_dict()
# create an instance of AddressRegistryAddVaultOptOutsRequest from a dict
address_registry_add_vault_opt_outs_request_from_dict = AddressRegistryAddVaultOptOutsRequest.from_dict(address_registry_add_vault_opt_outs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


