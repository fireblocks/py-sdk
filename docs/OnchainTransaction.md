# OnchainTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the transaction | 
**base_asset_id** | **str** | The blockchain base asset identifier | 
**block_hash** | **str** | Hash of the block containing this transaction | 
**block_number** | **int** | Block number containing this transaction | 
**block_timestamp** | **datetime** | Timestamp when the block was mined | 
**chain_id** | **int** | Chain ID of the blockchain | 
**contract_address** | **str** | Contract address if this is a contract transaction | [optional] 
**cumulative_gas_used** | **str** | Cumulative gas used in the block up to this transaction | 
**decoded_logs** | [**DecodedLog**](DecodedLog.md) |  | [optional] 
**effective_gas_price** | **str** | Effective gas price paid for the transaction | 
**from_address** | **str** | Address that initiated the transaction | 
**gas_used** | **str** | Amount of gas used by this transaction | 
**status** | **str** | Transaction status | 
**to_address** | **str** | Address that received the transaction | [optional] 
**transaction_hash** | **str** | Hash of the transaction | 
**transaction_index** | **str** | Index of the transaction in the block | 
**type** | **str** | Transaction type | 

## Example

```python
from fireblocks.models.onchain_transaction import OnchainTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainTransaction from a JSON string
onchain_transaction_instance = OnchainTransaction.from_json(json)
# print the JSON string representation of the object
print(OnchainTransaction.to_json())

# convert the object into a dict
onchain_transaction_dict = onchain_transaction_instance.to_dict()
# create an instance of OnchainTransaction from a dict
onchain_transaction_from_dict = OnchainTransaction.from_dict(onchain_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


