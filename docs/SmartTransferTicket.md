# SmartTransferTicket

Data object with result data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of Smart Transfer ticket | 
**type** | **str** | Kind of Smart Transfer. Can be either &#x60;ASYNC&#x60; or &#x60;ATOMIC&#x60; | 
**direction** | **str** | Direction of Smart Transfer. | [optional] 
**status** | **str** | Current status of Smart Transfer ticket | 
**terms** | [**List[SmartTransferTicketTerm]**](SmartTransferTicketTerm.md) | Ticket terms (legs) | [optional] 
**expires_in** | **float** | Number of hours for expiration.This data is valid only it ticket not in DRAFT state and it will be used to calculate expiresAt value | [optional] 
**expires_at** | **datetime** | Date and time at which the ticket will expire if no funding is performed. | [optional] 
**submitted_at** | **datetime** | Date and time when ticket is submitted. | [optional] 
**expired_at** | **datetime** | Date and time when ticket is expired. | [optional] 
**canceled_at** | **datetime** | Date and time when ticket is canceled. | [optional] 
**fulfilled_at** | **datetime** | Date and time when ticket is fulfilled. | [optional] 
**external_ref_id** | **str** | External Ref ID for Smart Transfer ticket. | [optional] 
**note** | **str** | Note | [optional] 
**created_by_network_id** | **str** | ID of network profile that created ticket | 
**created_by_network_id_name** | **str** | Name of network profile that created ticket | 
**canceled_by_network_id_name** | **str** | Name of network profile that canceled ticket | [optional] 
**created_at** | **datetime** | Date and time at which the ticket is created. | 
**updated_at** | **datetime** | Date and time of last ticket update. | 
**canceled_by_me** | **bool** |  | [optional] 
**created_by_me** | **bool** |  | [optional] 

## Example

```python
from fireblocks_client.models.smart_transfer_ticket import SmartTransferTicket

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferTicket from a JSON string
smart_transfer_ticket_instance = SmartTransferTicket.from_json(json)
# print the JSON string representation of the object
print(SmartTransferTicket.to_json())

# convert the object into a dict
smart_transfer_ticket_dict = smart_transfer_ticket_instance.to_dict()
# create an instance of SmartTransferTicket from a dict
smart_transfer_ticket_from_dict = SmartTransferTicket.from_dict(smart_transfer_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


