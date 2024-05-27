# FreezeTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 

## Example

```python
from fireblocks_client.models.freeze_transaction_response import FreezeTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FreezeTransactionResponse from a JSON string
freeze_transaction_response_instance = FreezeTransactionResponse.from_json(json)
# print the JSON string representation of the object
print FreezeTransactionResponse.to_json()

# convert the object into a dict
freeze_transaction_response_dict = freeze_transaction_response_instance.to_dict()
# create an instance of FreezeTransactionResponse from a dict
freeze_transaction_response_form_dict = freeze_transaction_response.from_dict(freeze_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


