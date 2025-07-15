# VaultAccountsTagAttachmentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_ids** | **List[str]** | The IDs of the tags to attach | 
**vault_account_ids** | **List[str]** | The IDs of the vault accounts to attach tags to | 

## Example

```python
from fireblocks.models.vault_accounts_tag_attachments_request import VaultAccountsTagAttachmentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VaultAccountsTagAttachmentsRequest from a JSON string
vault_accounts_tag_attachments_request_instance = VaultAccountsTagAttachmentsRequest.from_json(json)
# print the JSON string representation of the object
print(VaultAccountsTagAttachmentsRequest.to_json())

# convert the object into a dict
vault_accounts_tag_attachments_request_dict = vault_accounts_tag_attachments_request_instance.to_dict()
# create an instance of VaultAccountsTagAttachmentsRequest from a dict
vault_accounts_tag_attachments_request_from_dict = VaultAccountsTagAttachmentsRequest.from_dict(vault_accounts_tag_attachments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


