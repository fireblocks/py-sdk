# SmartTransferTicketFilteredResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message | 
**after** | **str** | Unique id of next filtered result | 
**data** | [**List[SmartTransferTicket]**](SmartTransferTicket.md) | Result that match given query criteria | 

## Example

```python
from fireblocks.models.smart_transfer_ticket_filtered_response import SmartTransferTicketFilteredResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferTicketFilteredResponse from a JSON string
smart_transfer_ticket_filtered_response_instance = SmartTransferTicketFilteredResponse.from_json(json)
# print the JSON string representation of the object
print(SmartTransferTicketFilteredResponse.to_json())

# convert the object into a dict
smart_transfer_ticket_filtered_response_dict = smart_transfer_ticket_filtered_response_instance.to_dict()
# create an instance of SmartTransferTicketFilteredResponse from a dict
smart_transfer_ticket_filtered_response_from_dict = SmartTransferTicketFilteredResponse.from_dict(smart_transfer_ticket_filtered_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


