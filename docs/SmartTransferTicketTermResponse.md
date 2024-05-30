# SmartTransferTicketTermResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message | 
**data** | [**SmartTransferTicketTerm**](SmartTransferTicketTerm.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.smart_transfer_ticket_term_response import SmartTransferTicketTermResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferTicketTermResponse from a JSON string
smart_transfer_ticket_term_response_instance = SmartTransferTicketTermResponse.from_json(json)
# print the JSON string representation of the object
print(SmartTransferTicketTermResponse.to_json())

# convert the object into a dict
smart_transfer_ticket_term_response_dict = smart_transfer_ticket_term_response_instance.to_dict()
# create an instance of SmartTransferTicketTermResponse from a dict
smart_transfer_ticket_term_response_from_dict = SmartTransferTicketTermResponse.from_dict(smart_transfer_ticket_term_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


