# UnfreezeTransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 

## Example

```python
from fireblocks_client.models.unfreeze_transaction_response import UnfreezeTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnfreezeTransactionResponse from a JSON string
unfreeze_transaction_response_instance = UnfreezeTransactionResponse.from_json(json)
# print the JSON string representation of the object
print UnfreezeTransactionResponse.to_json()

# convert the object into a dict
unfreeze_transaction_response_dict = unfreeze_transaction_response_instance.to_dict()
# create an instance of UnfreezeTransactionResponse from a dict
unfreeze_transaction_response_form_dict = unfreeze_transaction_response.from_dict(unfreeze_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


