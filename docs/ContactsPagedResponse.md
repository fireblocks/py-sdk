# ContactsPagedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Contact]**](Contact.md) | The page of contacts | 
**next** | **str** | Cursor to the next page; absent when the current page is the last. Opaque, and bound to the sort that minted it — replay it unchanged and keep sortBy/order steady across pages. | [optional] 
**total** | **int** | The number of contacts matching the filters, ignoring pagination. Present only when the request passed &#x60;includeTotal&#x3D;true&#x60;; the key is absent otherwise. | [optional] 

## Example

```python
from fireblocks.models.contacts_paged_response import ContactsPagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsPagedResponse from a JSON string
contacts_paged_response_instance = ContactsPagedResponse.from_json(json)
# print the JSON string representation of the object
print(ContactsPagedResponse.to_json())

# convert the object into a dict
contacts_paged_response_dict = contacts_paged_response_instance.to_dict()
# create an instance of ContactsPagedResponse from a dict
contacts_paged_response_from_dict = ContactsPagedResponse.from_dict(contacts_paged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


