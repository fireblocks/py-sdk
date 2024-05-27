# SmartTransferCreateTicketTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | Asset name | 
**amount** | **float** | Amount | 
**from_network_id** | **str** | Identifier of the origination Network Profile | 
**to_network_id** | **str** | Identifier of the destination Network Profile | 

## Example

```python
from fireblocks_client.models.smart_transfer_create_ticket_term import SmartTransferCreateTicketTerm

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferCreateTicketTerm from a JSON string
smart_transfer_create_ticket_term_instance = SmartTransferCreateTicketTerm.from_json(json)
# print the JSON string representation of the object
print SmartTransferCreateTicketTerm.to_json()

# convert the object into a dict
smart_transfer_create_ticket_term_dict = smart_transfer_create_ticket_term_instance.to_dict()
# create an instance of SmartTransferCreateTicketTerm from a dict
smart_transfer_create_ticket_term_form_dict = smart_transfer_create_ticket_term.from_dict(smart_transfer_create_ticket_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


