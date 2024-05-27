# SmartTransferCreateTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_network_id** | **str** |  | 
**type** | **str** |  | 
**expires_in** | **float** | Number of hours after which an OPEN ticket will expire if no term is funded. | [optional] 
**terms** | [**List[SmartTransferCreateTicketTerm]**](SmartTransferCreateTicketTerm.md) |  | [optional] 
**external_ref_id** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**submit** | **bool** |  | [optional] 

## Example

```python
from fireblocks_client.models.smart_transfer_create_ticket import SmartTransferCreateTicket

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferCreateTicket from a JSON string
smart_transfer_create_ticket_instance = SmartTransferCreateTicket.from_json(json)
# print the JSON string representation of the object
print SmartTransferCreateTicket.to_json()

# convert the object into a dict
smart_transfer_create_ticket_dict = smart_transfer_create_ticket_instance.to_dict()
# create an instance of SmartTransferCreateTicket from a dict
smart_transfer_create_ticket_form_dict = smart_transfer_create_ticket.from_dict(smart_transfer_create_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


