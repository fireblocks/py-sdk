# AddressRegistryListVaultOptOutsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of vault accounts excluded from the address registry for your workspace. | 
**data** | [**List[AddressRegistryVaultOptOutItem]**](AddressRegistryVaultOptOutItem.md) |  | 
**next** | **str** | Opaque cursor for the next page; empty when there is no next page. | [optional] 
**prev** | **str** | Opaque cursor for the previous page; empty when there is no previous page. | [optional] 

## Example

```python
from fireblocks.models.address_registry_list_vault_opt_outs_response import AddressRegistryListVaultOptOutsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryListVaultOptOutsResponse from a JSON string
address_registry_list_vault_opt_outs_response_instance = AddressRegistryListVaultOptOutsResponse.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryListVaultOptOutsResponse.to_json())

# convert the object into a dict
address_registry_list_vault_opt_outs_response_dict = address_registry_list_vault_opt_outs_response_instance.to_dict()
# create an instance of AddressRegistryListVaultOptOutsResponse from a dict
address_registry_list_vault_opt_outs_response_from_dict = AddressRegistryListVaultOptOutsResponse.from_dict(address_registry_list_vault_opt_outs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


