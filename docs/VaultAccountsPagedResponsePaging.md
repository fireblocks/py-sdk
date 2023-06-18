# VaultAccountsPagedResponsePaging


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | **str** |  | [optional] 
**after** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.vault_accounts_paged_response_paging import VaultAccountsPagedResponsePaging

# TODO update the JSON string below
json = "{}"
# create an instance of VaultAccountsPagedResponsePaging from a JSON string
vault_accounts_paged_response_paging_instance = VaultAccountsPagedResponsePaging.from_json(json)
# print the JSON string representation of the object
print VaultAccountsPagedResponsePaging.to_json()

# convert the object into a dict
vault_accounts_paged_response_paging_dict = vault_accounts_paged_response_paging_instance.to_dict()
# create an instance of VaultAccountsPagedResponsePaging from a dict
vault_accounts_paged_response_paging_form_dict = vault_accounts_paged_response_paging.from_dict(vault_accounts_paged_response_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


