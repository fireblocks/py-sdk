# VaultAccountTagAttachmentOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The ID of the vault account | 
**tag_id** | **str** | Tag ID | 
**action** | [**TagAttachmentOperationAction**](TagAttachmentOperationAction.md) |  | 

## Example

```python
from fireblocks.models.vault_account_tag_attachment_operation import VaultAccountTagAttachmentOperation

# TODO update the JSON string below
json = "{}"
# create an instance of VaultAccountTagAttachmentOperation from a JSON string
vault_account_tag_attachment_operation_instance = VaultAccountTagAttachmentOperation.from_json(json)
# print the JSON string representation of the object
print(VaultAccountTagAttachmentOperation.to_json())

# convert the object into a dict
vault_account_tag_attachment_operation_dict = vault_account_tag_attachment_operation_instance.to_dict()
# create an instance of VaultAccountTagAttachmentOperation from a dict
vault_account_tag_attachment_operation_from_dict = VaultAccountTagAttachmentOperation.from_dict(vault_account_tag_attachment_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


