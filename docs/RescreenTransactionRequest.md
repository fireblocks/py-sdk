# RescreenTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reset_travel_rule_message** | **bool** | When true, clears the existing travel rule message on the transaction before rescreening. | [optional] [default to False]

## Example

```python
from fireblocks.models.rescreen_transaction_request import RescreenTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RescreenTransactionRequest from a JSON string
rescreen_transaction_request_instance = RescreenTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(RescreenTransactionRequest.to_json())

# convert the object into a dict
rescreen_transaction_request_dict = rescreen_transaction_request_instance.to_dict()
# create an instance of RescreenTransactionRequest from a dict
rescreen_transaction_request_from_dict = RescreenTransactionRequest.from_dict(rescreen_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


