# TransactionRequestPriorityFee

For Ethereum-based blockchains only, the fee for EIP-1559 transaction pricing mechanism. Value is in Gwei.  Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fireblocks_client.models.transaction_request_priority_fee import TransactionRequestPriorityFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestPriorityFee from a JSON string
transaction_request_priority_fee_instance = TransactionRequestPriorityFee.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestPriorityFee.to_json())

# convert the object into a dict
transaction_request_priority_fee_dict = transaction_request_priority_fee_instance.to_dict()
# create an instance of TransactionRequestPriorityFee from a dict
transaction_request_priority_fee_from_dict = TransactionRequestPriorityFee.from_dict(transaction_request_priority_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


