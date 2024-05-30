# EstimatedTransactionFeeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**low** | [**TransactionFee**](TransactionFee.md) |  | 
**medium** | [**TransactionFee**](TransactionFee.md) |  | 
**high** | [**TransactionFee**](TransactionFee.md) |  | 

## Example

```python
from fireblocks_client.models.estimated_transaction_fee_response import EstimatedTransactionFeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedTransactionFeeResponse from a JSON string
estimated_transaction_fee_response_instance = EstimatedTransactionFeeResponse.from_json(json)
# print the JSON string representation of the object
print(EstimatedTransactionFeeResponse.to_json())

# convert the object into a dict
estimated_transaction_fee_response_dict = estimated_transaction_fee_response_instance.to_dict()
# create an instance of EstimatedTransactionFeeResponse from a dict
estimated_transaction_fee_response_from_dict = EstimatedTransactionFeeResponse.from_dict(estimated_transaction_fee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


