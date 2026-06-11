# TransactionConfigurations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_after_seconds** | **float** | The number of seconds the transaction is valid for before it expires. After the specified duration, the transaction will expire if it has not been broadcasted. | [optional] 

## Example

```python
from fireblocks.models.transaction_configurations import TransactionConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionConfigurations from a JSON string
transaction_configurations_instance = TransactionConfigurations.from_json(json)
# print the JSON string representation of the object
print(TransactionConfigurations.to_json())

# convert the object into a dict
transaction_configurations_dict = transaction_configurations_instance.to_dict()
# create an instance of TransactionConfigurations from a dict
transaction_configurations_from_dict = TransactionConfigurations.from_dict(transaction_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


