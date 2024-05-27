# SmartTransferSetTicketExpiration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_in** | **float** | Sets ticket expiration time (in hours) after a ticket is submitted. If no funding source is set to any term, the ticket will automatically expire after given time. | 

## Example

```python
from fireblocks_client.models.smart_transfer_set_ticket_expiration import SmartTransferSetTicketExpiration

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferSetTicketExpiration from a JSON string
smart_transfer_set_ticket_expiration_instance = SmartTransferSetTicketExpiration.from_json(json)
# print the JSON string representation of the object
print SmartTransferSetTicketExpiration.to_json()

# convert the object into a dict
smart_transfer_set_ticket_expiration_dict = smart_transfer_set_ticket_expiration_instance.to_dict()
# create an instance of SmartTransferSetTicketExpiration from a dict
smart_transfer_set_ticket_expiration_form_dict = smart_transfer_set_ticket_expiration.from_dict(smart_transfer_set_ticket_expiration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


