# ContactTagAttachmentPending

An attach or detach of this tag to this contact awaiting a quorum decision. Null when the attachment is settled. Distinct from the tag's own `pendingApprovalRequest`, which covers a change to the tag itself rather than to this pairing. When both are open, this is the one to act on from a contact: cancelling a change to the tag's own definition belongs to the tag surface, and `pendingApprovalRequest.id` must not be used to cancel an attachment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The operation awaiting approval. ATTACH means the tag is not yet attached; DETACH means it is still attached, pending removal. | 
**approval_request_id** | **str** | The identifier of the approval request gating the operation | [optional] 

## Example

```python
from fireblocks.models.contact_tag_attachment_pending import ContactTagAttachmentPending

# TODO update the JSON string below
json = "{}"
# create an instance of ContactTagAttachmentPending from a JSON string
contact_tag_attachment_pending_instance = ContactTagAttachmentPending.from_json(json)
# print the JSON string representation of the object
print(ContactTagAttachmentPending.to_json())

# convert the object into a dict
contact_tag_attachment_pending_dict = contact_tag_attachment_pending_instance.to_dict()
# create an instance of ContactTagAttachmentPending from a dict
contact_tag_attachment_pending_from_dict = ContactTagAttachmentPending.from_dict(contact_tag_attachment_pending_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


