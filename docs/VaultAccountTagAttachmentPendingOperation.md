# VaultAccountTagAttachmentPendingOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The ID of the vault account | 
**tag_id** | **str** | Tag ID | 
**action** | [**TagAttachmentOperationAction**](TagAttachmentOperationAction.md) |  | 
**approval_request_id** | **str** | Pending approval request ID | 

## Example

```python
from fireblocks.models.vault_account_tag_attachment_pending_operation import VaultAccountTagAttachmentPendingOperation

# TODO update the JSON string below
json = "{}"
# create an instance of VaultAccountTagAttachmentPendingOperation from a JSON string
vault_account_tag_attachment_pending_operation_instance = VaultAccountTagAttachmentPendingOperation.from_json(json)
# print the JSON string representation of the object
print(VaultAccountTagAttachmentPendingOperation.to_json())

# convert the object into a dict
vault_account_tag_attachment_pending_operation_dict = vault_account_tag_attachment_pending_operation_instance.to_dict()
# create an instance of VaultAccountTagAttachmentPendingOperation from a dict
vault_account_tag_attachment_pending_operation_from_dict = VaultAccountTagAttachmentPendingOperation.from_dict(vault_account_tag_attachment_pending_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


