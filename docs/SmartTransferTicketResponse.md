# SmartTransferTicketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message | 
**data** | [**SmartTransferTicket**](SmartTransferTicket.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.smart_transfer_ticket_response import SmartTransferTicketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferTicketResponse from a JSON string
smart_transfer_ticket_response_instance = SmartTransferTicketResponse.from_json(json)
# print the JSON string representation of the object
print(SmartTransferTicketResponse.to_json())

# convert the object into a dict
smart_transfer_ticket_response_dict = smart_transfer_ticket_response_instance.to_dict()
# create an instance of SmartTransferTicketResponse from a dict
smart_transfer_ticket_response_from_dict = SmartTransferTicketResponse.from_dict(smart_transfer_ticket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


