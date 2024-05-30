# TransactionRequestGasLimit

For EVM-based blockchains only. Units of gas required to process the transaction. Note: Only two of the three arguments can be specified in a single transaction: `gasLimit`, `gasPrice` and `networkFee`. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fireblocks.models.transaction_request_gas_limit import TransactionRequestGasLimit

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestGasLimit from a JSON string
transaction_request_gas_limit_instance = TransactionRequestGasLimit.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestGasLimit.to_json())

# convert the object into a dict
transaction_request_gas_limit_dict = transaction_request_gas_limit_instance.to_dict()
# create an instance of TransactionRequestGasLimit from a dict
transaction_request_gas_limit_from_dict = TransactionRequestGasLimit.from_dict(transaction_request_gas_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


