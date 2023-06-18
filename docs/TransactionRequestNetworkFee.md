# TransactionRequestNetworkFee

For EVM-based blockchains only. The total transaction fee in the blockchain’s largest unit. Note: Only two of the three arguments can be specified in a single transaction: `gasLimit`, `gasPrice` and `networkFee`. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. - The transaction blockchain fee. - For Ethereum, you can't pass gasPrice, gasLimit and networkFee all together. - A numeric value representation is required.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fireblocks_client.models.transaction_request_network_fee import TransactionRequestNetworkFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestNetworkFee from a JSON string
transaction_request_network_fee_instance = TransactionRequestNetworkFee.from_json(json)
# print the JSON string representation of the object
print TransactionRequestNetworkFee.to_json()

# convert the object into a dict
transaction_request_network_fee_dict = transaction_request_network_fee_instance.to_dict()
# create an instance of TransactionRequestNetworkFee from a dict
transaction_request_network_fee_form_dict = transaction_request_network_fee.from_dict(transaction_request_network_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


