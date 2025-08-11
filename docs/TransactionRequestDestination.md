# TransactionRequestDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**destination** | [**DestinationTransferPeerPath**](DestinationTransferPeerPath.md) |  | [optional] 
**travel_rule_message_id** | **str** | The ID of the travel rule message from any travel rule provider. Used for travel rule linking functionality to associate transactions with existing travel rule messages. | [optional] 
**customer_ref_id** | **str** | The ID for AML providers to associate the owner of funds with transactions. | [optional] 

## Example

```python
from fireblocks.models.transaction_request_destination import TransactionRequestDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestDestination from a JSON string
transaction_request_destination_instance = TransactionRequestDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestDestination.to_json())

# convert the object into a dict
transaction_request_destination_dict = transaction_request_destination_instance.to_dict()
# create an instance of TransactionRequestDestination from a dict
transaction_request_destination_from_dict = TransactionRequestDestination.from_dict(transaction_request_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


