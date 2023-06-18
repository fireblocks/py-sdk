# CancelTransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 

## Example

```python
from fireblocks_client.models.cancel_transaction_response import CancelTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelTransactionResponse from a JSON string
cancel_transaction_response_instance = CancelTransactionResponse.from_json(json)
# print the JSON string representation of the object
print CancelTransactionResponse.to_json()

# convert the object into a dict
cancel_transaction_response_dict = cancel_transaction_response_instance.to_dict()
# create an instance of CancelTransactionResponse from a dict
cancel_transaction_response_form_dict = cancel_transaction_response.from_dict(cancel_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


