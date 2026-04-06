# AddressRegistryAddVaultOptOutsResponse

Result of adding vault account ids to the workspace opt-out list for the address registry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_count** | **int** | Number of vault ids from the request that were processed. An empty &#x60;vaultAccountIds&#x60; list is rejected with HTTP 400, not a 200 with zero. | 

## Example

```python
from fireblocks.models.address_registry_add_vault_opt_outs_response import AddressRegistryAddVaultOptOutsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryAddVaultOptOutsResponse from a JSON string
address_registry_add_vault_opt_outs_response_instance = AddressRegistryAddVaultOptOutsResponse.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryAddVaultOptOutsResponse.to_json())

# convert the object into a dict
address_registry_add_vault_opt_outs_response_dict = address_registry_add_vault_opt_outs_response_instance.to_dict()
# create an instance of AddressRegistryAddVaultOptOutsResponse from a dict
address_registry_add_vault_opt_outs_response_from_dict = AddressRegistryAddVaultOptOutsResponse.from_dict(address_registry_add_vault_opt_outs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


