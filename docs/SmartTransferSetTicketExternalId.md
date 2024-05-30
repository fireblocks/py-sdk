# SmartTransferSetTicketExternalId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_ref_id** | **str** | Each workspace can set their own external id they want to refer to this Ticket | 

## Example

```python
from fireblocks.models.smart_transfer_set_ticket_external_id import SmartTransferSetTicketExternalId

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferSetTicketExternalId from a JSON string
smart_transfer_set_ticket_external_id_instance = SmartTransferSetTicketExternalId.from_json(json)
# print the JSON string representation of the object
print(SmartTransferSetTicketExternalId.to_json())

# convert the object into a dict
smart_transfer_set_ticket_external_id_dict = smart_transfer_set_ticket_external_id_instance.to_dict()
# create an instance of SmartTransferSetTicketExternalId from a dict
smart_transfer_set_ticket_external_id_from_dict = SmartTransferSetTicketExternalId.from_dict(smart_transfer_set_ticket_external_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


