# TransactionRequestGasPrice

For non-EIP-1559, EVM-based transactions. Price per gas unit (in Ethereum this is specified in Gwei).  Note: Only two of the three arguments can be specified in a single transaction: `gasLimit`, `gasPrice` and `networkFee`. Fireblocks recommends using a numeric string for accurate precision.  Although a number input exists, it is deprecated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fireblocks_client.models.transaction_request_gas_price import TransactionRequestGasPrice

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestGasPrice from a JSON string
transaction_request_gas_price_instance = TransactionRequestGasPrice.from_json(json)
# print the JSON string representation of the object
print TransactionRequestGasPrice.to_json()

# convert the object into a dict
transaction_request_gas_price_dict = transaction_request_gas_price_instance.to_dict()
# create an instance of TransactionRequestGasPrice from a dict
transaction_request_gas_price_form_dict = transaction_request_gas_price.from_dict(transaction_request_gas_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


