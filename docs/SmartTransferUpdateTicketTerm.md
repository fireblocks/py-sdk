# SmartTransferUpdateTicketTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | Asset name | 
**amount** | **float** | Amount | 
**from_network_id** | **str** | Identifier of the origination Network Profile | 
**to_network_id** | **str** | Identifier of the destination Network Profile | 

## Example

```python
from fireblocks_client.models.smart_transfer_update_ticket_term import SmartTransferUpdateTicketTerm

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferUpdateTicketTerm from a JSON string
smart_transfer_update_ticket_term_instance = SmartTransferUpdateTicketTerm.from_json(json)
# print the JSON string representation of the object
print(SmartTransferUpdateTicketTerm.to_json())

# convert the object into a dict
smart_transfer_update_ticket_term_dict = smart_transfer_update_ticket_term_instance.to_dict()
# create an instance of SmartTransferUpdateTicketTerm from a dict
smart_transfer_update_ticket_term_from_dict = SmartTransferUpdateTicketTerm.from_dict(smart_transfer_update_ticket_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


