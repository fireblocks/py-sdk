# TransactionResponseDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_address** | **object** | Address where the asset was transferred. | [optional] 
**destination_address_description** | **object** | Description of the address. | [optional] 
**amount** | **str** | The amount to be sent to this destination. | [optional] 
**amount_usd** | **str** | The USD value of the requested amount. | [optional] 
**aml_screening_result** | [**AmlScreeningResult**](AmlScreeningResult.md) |  | [optional] 
**destination** | [**DestinationTransferPeerPathResponse**](DestinationTransferPeerPathResponse.md) |  | [optional] 
**authorization_info** | [**AuthorizationInfo**](AuthorizationInfo.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.transaction_response_destination import TransactionResponseDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponseDestination from a JSON string
transaction_response_destination_instance = TransactionResponseDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionResponseDestination.to_json())

# convert the object into a dict
transaction_response_destination_dict = transaction_response_destination_instance.to_dict()
# create an instance of TransactionResponseDestination from a dict
transaction_response_destination_from_dict = TransactionResponseDestination.from_dict(transaction_response_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


