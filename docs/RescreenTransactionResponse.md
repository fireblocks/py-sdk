# RescreenTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the rescreen was triggered successfully | 

## Example

```python
from fireblocks.models.rescreen_transaction_response import RescreenTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RescreenTransactionResponse from a JSON string
rescreen_transaction_response_instance = RescreenTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(RescreenTransactionResponse.to_json())

# convert the object into a dict
rescreen_transaction_response_dict = rescreen_transaction_response_instance.to_dict()
# create an instance of RescreenTransactionResponse from a dict
rescreen_transaction_response_from_dict = RescreenTransactionResponse.from_dict(rescreen_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


