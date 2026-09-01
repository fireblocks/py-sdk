# ContactTag

A tag attached to the contact, with the display details resolved from the tagging service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the tag | 
**label** | **str** | The tag label | 
**color** | **str** | The tag color in hex format. Absent when the tag has none. | [optional] 
**description** | **str** | Description for the tag. Absent when the tag has none. | [optional] 
**is_protected** | **bool** | Whether the tag is protected, meaning changes to it and to its attachments are approval-gated. | 
**pending_approval_request** | [**ContactApprovalRequest**](ContactApprovalRequest.md) |  | 
**pending_attachment** | [**ContactTagAttachmentPending**](ContactTagAttachmentPending.md) |  | 

## Example

```python
from fireblocks.models.contact_tag import ContactTag

# TODO update the JSON string below
json = "{}"
# create an instance of ContactTag from a JSON string
contact_tag_instance = ContactTag.from_json(json)
# print the JSON string representation of the object
print(ContactTag.to_json())

# convert the object into a dict
contact_tag_dict = contact_tag_instance.to_dict()
# create an instance of ContactTag from a dict
contact_tag_from_dict = ContactTag.from_dict(contact_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


