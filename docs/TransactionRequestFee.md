# TransactionRequestFee

For UTXO-based blockchains, the fee per bytes in the asset’s smallest unit (Satoshi, Latoshi, etc.).  For Ripple, the fee for the transaction. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fireblocks.models.transaction_request_fee import TransactionRequestFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestFee from a JSON string
transaction_request_fee_instance = TransactionRequestFee.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestFee.to_json())

# convert the object into a dict
transaction_request_fee_dict = transaction_request_fee_instance.to_dict()
# create an instance of TransactionRequestFee from a dict
transaction_request_fee_from_dict = TransactionRequestFee.from_dict(transaction_request_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


