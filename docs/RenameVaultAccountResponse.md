# RenameVaultAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the vault account | [optional] 
**id** | **str** | The ID of the vault account | [optional] 

## Example

```python
from fireblocks_client.models.rename_vault_account_response import RenameVaultAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RenameVaultAccountResponse from a JSON string
rename_vault_account_response_instance = RenameVaultAccountResponse.from_json(json)
# print the JSON string representation of the object
print(RenameVaultAccountResponse.to_json())

# convert the object into a dict
rename_vault_account_response_dict = rename_vault_account_response_instance.to_dict()
# create an instance of RenameVaultAccountResponse from a dict
rename_vault_account_response_from_dict = RenameVaultAccountResponse.from_dict(rename_vault_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


