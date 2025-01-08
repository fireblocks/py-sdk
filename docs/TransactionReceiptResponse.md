# TransactionReceiptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_hash** | **str** | The block hash | 
**block_number** | **int** | The block number | 
**contract_address** | **str** | The address of deployed contract | [optional] 
**cumulative_gas_used** | **int** | The cumulative gas used in the transaction | 
**effective_gas_price** | **int** | The effective gas price | 
**var_from** | **str** | Sender address | 
**gas_used** | **int** | Gas used by the transaction | 
**logs** | [**List[TxLog]**](TxLog.md) | Array of transaction logs | 
**logs_bloom** | **str** | Logs bloom filter | 
**status** | **int** | Transaction status (1 for success, 0 for failure) | 
**to** | **str** | Recipient address | [optional] 
**transaction_hash** | **str** | The transaction hash | 
**transaction_index** | **int** | Transaction index in the block | 
**type** | **str** | Type of transaction | 

## Example

```python
from fireblocks.models.transaction_receipt_response import TransactionReceiptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReceiptResponse from a JSON string
transaction_receipt_response_instance = TransactionReceiptResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionReceiptResponse.to_json())

# convert the object into a dict
transaction_receipt_response_dict = transaction_receipt_response_instance.to_dict()
# create an instance of TransactionReceiptResponse from a dict
transaction_receipt_response_from_dict = TransactionReceiptResponse.from_dict(transaction_receipt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


