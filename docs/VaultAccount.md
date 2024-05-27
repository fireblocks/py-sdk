# VaultAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**assets** | [**List[VaultAsset]**](VaultAsset.md) |  | [optional] 
**hidden_on_ui** | **bool** |  | [optional] 
**customer_ref_id** | **str** |  | [optional] 
**auto_fuel** | **bool** |  | [optional] 

## Example

```python
from fireblocks_client.models.vault_account import VaultAccount

# TODO update the JSON string below
json = "{}"
# create an instance of VaultAccount from a JSON string
vault_account_instance = VaultAccount.from_json(json)
# print the JSON string representation of the object
print VaultAccount.to_json()

# convert the object into a dict
vault_account_dict = vault_account_instance.to_dict()
# create an instance of VaultAccount from a dict
vault_account_form_dict = vault_account.from_dict(vault_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


