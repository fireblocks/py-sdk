# VaultAccountsPagedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[VaultAccount]**](VaultAccount.md) |  | [optional] 
**paging** | [**VaultAccountsPagedResponsePaging**](VaultAccountsPagedResponsePaging.md) |  | [optional] 
**previous_url** | **str** |  | [optional] 
**next_url** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.vault_accounts_paged_response import VaultAccountsPagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VaultAccountsPagedResponse from a JSON string
vault_accounts_paged_response_instance = VaultAccountsPagedResponse.from_json(json)
# print the JSON string representation of the object
print(VaultAccountsPagedResponse.to_json())

# convert the object into a dict
vault_accounts_paged_response_dict = vault_accounts_paged_response_instance.to_dict()
# create an instance of VaultAccountsPagedResponse from a dict
vault_accounts_paged_response_from_dict = VaultAccountsPagedResponse.from_dict(vault_accounts_paged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


