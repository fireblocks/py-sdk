# Contact

A contact in the workspace address book.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the contact | 
**name** | **str** | The contact name, unique across the workspace | 
**type** | **str** | Whether the contact is an external party or an account the workspace owns elsewhere | 
**access_control** | **str** | The access control applied to the contact. Absent when none is set. | [optional] 
**notes** | **str** | Free-text notes on the contact. Absent when none are set. | [optional] 
**external_ref_id** | **str** | A customer-supplied reference id for the contact. Absent when none is set. | [optional] 
**container_id** | **str** | The container holding the contact. Absent when the contact sits at the root. | [optional] 
**updated_at** | **datetime** | The date and time the contact was last modified, in ISO-8601 | 
**archived_at** | **datetime** | The date and time the contact was archived, in ISO-8601. Absent for live contacts, so this only carries a value when the request passed archived&#x3D;true. | [optional] 
**tags** | [**List[ContactTag]**](ContactTag.md) | The tags attached to the contact | 
**pending_approval_request** | [**ContactApprovalRequest**](ContactApprovalRequest.md) |  | 

## Example

```python
from fireblocks.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print(Contact.to_json())

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_from_dict = Contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


