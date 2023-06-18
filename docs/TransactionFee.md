# TransactionFee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_per_byte** | **str** |  | [optional] 
**gas_price** | **str** |  | [optional] 
**gas_limit** | **str** |  | [optional] 
**network_fee** | **str** |  | [optional] 
**base_fee** | **str** | (optional) Base Fee according to EIP-1559 (ETH assets) | [optional] 
**priority_fee** | **str** | (optional) Priority Fee according to EIP-1559 (ETH assets) | [optional] 

## Example

```python
from fireblocks_client.models.transaction_fee import TransactionFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFee from a JSON string
transaction_fee_instance = TransactionFee.from_json(json)
# print the JSON string representation of the object
print TransactionFee.to_json()

# convert the object into a dict
transaction_fee_dict = transaction_fee_instance.to_dict()
# create an instance of TransactionFee from a dict
transaction_fee_form_dict = transaction_fee.from_dict(transaction_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


