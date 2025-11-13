# VaultAccountsTagAttachmentOperationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_operations** | [**List[VaultAccountTagAttachmentOperation]**](VaultAccountTagAttachmentOperation.md) | The operations that were applied | [optional] 
**pending_operations** | [**List[VaultAccountTagAttachmentPendingOperation]**](VaultAccountTagAttachmentPendingOperation.md) | The operations that are pending | [optional] 
**rejected_operations** | [**List[VaultAccountTagAttachmentRejectedOperation]**](VaultAccountTagAttachmentRejectedOperation.md) | The operations that were rejected | [optional] 

## Example

```python
from fireblocks.models.vault_accounts_tag_attachment_operations_response import VaultAccountsTagAttachmentOperationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VaultAccountsTagAttachmentOperationsResponse from a JSON string
vault_accounts_tag_attachment_operations_response_instance = VaultAccountsTagAttachmentOperationsResponse.from_json(json)
# print the JSON string representation of the object
print(VaultAccountsTagAttachmentOperationsResponse.to_json())

# convert the object into a dict
vault_accounts_tag_attachment_operations_response_dict = vault_accounts_tag_attachment_operations_response_instance.to_dict()
# create an instance of VaultAccountsTagAttachmentOperationsResponse from a dict
vault_accounts_tag_attachment_operations_response_from_dict = VaultAccountsTagAttachmentOperationsResponse.from_dict(vault_accounts_tag_attachment_operations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


