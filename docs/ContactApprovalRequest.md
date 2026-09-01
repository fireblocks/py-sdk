# ContactApprovalRequest

An approval request awaiting a quorum decision. Null when none is open. Carried both by a contact, for a quorum-gated write on the contact itself, and by an individual tag, for a change to the tag's own definition. An attach or detach of that tag to this contact is carried by the tag's `pendingAttachment` instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The approval request identifier | 
**type** | **str** | The operation awaiting approval. Deliberately not an enumeration: the set is open across the surfaces that carry one, and includes contact operations such as CREATE_CONTACT and DELETE_CONTACT as well as changes to a tag itself. | 

## Example

```python
from fireblocks.models.contact_approval_request import ContactApprovalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContactApprovalRequest from a JSON string
contact_approval_request_instance = ContactApprovalRequest.from_json(json)
# print the JSON string representation of the object
print(ContactApprovalRequest.to_json())

# convert the object into a dict
contact_approval_request_dict = contact_approval_request_instance.to_dict()
# create an instance of ContactApprovalRequest from a dict
contact_approval_request_from_dict = ContactApprovalRequest.from_dict(contact_approval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


