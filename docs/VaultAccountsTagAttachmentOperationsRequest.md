# VaultAccountsTagAttachmentOperationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_ids** | **List[str]** | The IDs of the vault accounts to attach tags to | 
**tag_ids_to_attach** | **List[str]** | The IDs of the tags to attach | [optional] 
**tag_ids_to_detach** | **List[str]** | The IDs of the tags to detach | [optional] 

## Example

```python
from fireblocks.models.vault_accounts_tag_attachment_operations_request import VaultAccountsTagAttachmentOperationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VaultAccountsTagAttachmentOperationsRequest from a JSON string
vault_accounts_tag_attachment_operations_request_instance = VaultAccountsTagAttachmentOperationsRequest.from_json(json)
# print the JSON string representation of the object
print(VaultAccountsTagAttachmentOperationsRequest.to_json())

# convert the object into a dict
vault_accounts_tag_attachment_operations_request_dict = vault_accounts_tag_attachment_operations_request_instance.to_dict()
# create an instance of VaultAccountsTagAttachmentOperationsRequest from a dict
vault_accounts_tag_attachment_operations_request_from_dict = VaultAccountsTagAttachmentOperationsRequest.from_dict(vault_accounts_tag_attachment_operations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


