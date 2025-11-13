# VaultAccountTagAttachmentRejectedOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The ID of the vault account | 
**tag_id** | **str** | Tag ID | 
**action** | [**TagAttachmentOperationAction**](TagAttachmentOperationAction.md) |  | 
**reason** | **str** | Reason for rejection | 

## Example

```python
from fireblocks.models.vault_account_tag_attachment_rejected_operation import VaultAccountTagAttachmentRejectedOperation

# TODO update the JSON string below
json = "{}"
# create an instance of VaultAccountTagAttachmentRejectedOperation from a JSON string
vault_account_tag_attachment_rejected_operation_instance = VaultAccountTagAttachmentRejectedOperation.from_json(json)
# print the JSON string representation of the object
print(VaultAccountTagAttachmentRejectedOperation.to_json())

# convert the object into a dict
vault_account_tag_attachment_rejected_operation_dict = vault_account_tag_attachment_rejected_operation_instance.to_dict()
# create an instance of VaultAccountTagAttachmentRejectedOperation from a dict
vault_account_tag_attachment_rejected_operation_from_dict = VaultAccountTagAttachmentRejectedOperation.from_dict(vault_account_tag_attachment_rejected_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


