# SmartTransferTicketTerm

Data object with result data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of Smart Transfer ticket term | 
**ticket_id** | **str** | Unique id of Smart Transfer ticket | 
**asset** | **str** | Asset name | 
**amount** | **str** | Amount | 
**amount_usd** | **str** | Amount USD | [optional] 
**from_network_id** | **str** | Identifier of the origination Network Profile | 
**from_network_id_name** | **str** | Source network name | 
**to_network_id** | **str** | Identifier of the destination Network Profile | 
**to_network_id_name** | **str** | Destination network name | 
**tx_hash** | **str** | Blockchain TX hash | 
**fb_tx_id** | **str** | Fireblocks transaction ID. It is set when the funding transaction is created. | 
**tx_status** | **str** | Ticket term transaction status | 
**status** | **str** | Ticket term status | 
**created_at** | **datetime** | Date and time when the term is created. | 
**updated_at** | **datetime** | Date and time of last term update. | 

## Example

```python
from fireblocks_client.models.smart_transfer_ticket_term import SmartTransferTicketTerm

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferTicketTerm from a JSON string
smart_transfer_ticket_term_instance = SmartTransferTicketTerm.from_json(json)
# print the JSON string representation of the object
print SmartTransferTicketTerm.to_json()

# convert the object into a dict
smart_transfer_ticket_term_dict = smart_transfer_ticket_term_instance.to_dict()
# create an instance of SmartTransferTicketTerm from a dict
smart_transfer_ticket_term_form_dict = smart_transfer_ticket_term.from_dict(smart_transfer_ticket_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


