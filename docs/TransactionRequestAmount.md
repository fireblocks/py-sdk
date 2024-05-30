# TransactionRequestAmount

For `TRANSFER` operations, the requested amount to transfer, in the asset’s unit. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fireblocks_client.models.transaction_request_amount import TransactionRequestAmount

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestAmount from a JSON string
transaction_request_amount_instance = TransactionRequestAmount.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestAmount.to_json())

# convert the object into a dict
transaction_request_amount_dict = transaction_request_amount_instance.to_dict()
# create an instance of TransactionRequestAmount from a dict
transaction_request_amount_from_dict = TransactionRequestAmount.from_dict(transaction_request_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


