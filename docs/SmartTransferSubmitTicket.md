# SmartTransferSubmitTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_in** | **float** | Sets the ticket expiration time (in hours) after the ticket is submitted. If no funding source is set for any term, the ticket will automatically expire after given time. If expiresIn is not sent ticket will not expire. | [optional] 

## Example

```python
from fireblocks_client.models.smart_transfer_submit_ticket import SmartTransferSubmitTicket

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferSubmitTicket from a JSON string
smart_transfer_submit_ticket_instance = SmartTransferSubmitTicket.from_json(json)
# print the JSON string representation of the object
print SmartTransferSubmitTicket.to_json()

# convert the object into a dict
smart_transfer_submit_ticket_dict = smart_transfer_submit_ticket_instance.to_dict()
# create an instance of SmartTransferSubmitTicket from a dict
smart_transfer_submit_ticket_form_dict = smart_transfer_submit_ticket.from_dict(smart_transfer_submit_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


