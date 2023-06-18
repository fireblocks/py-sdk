# TransactionResponseContractCallDecodedData

Decoded data for `CONTRACT_CALL` operations. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for setting this parameter's value.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_name** | **str** |  | [optional] 
**function_calls** | **List[object]** |  | [optional] 

## Example

```python
from fireblocks_client.models.transaction_response_contract_call_decoded_data import TransactionResponseContractCallDecodedData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponseContractCallDecodedData from a JSON string
transaction_response_contract_call_decoded_data_instance = TransactionResponseContractCallDecodedData.from_json(json)
# print the JSON string representation of the object
print TransactionResponseContractCallDecodedData.to_json()

# convert the object into a dict
transaction_response_contract_call_decoded_data_dict = transaction_response_contract_call_decoded_data_instance.to_dict()
# create an instance of TransactionResponseContractCallDecodedData from a dict
transaction_response_contract_call_decoded_data_form_dict = transaction_response_contract_call_decoded_data.from_dict(transaction_response_contract_call_decoded_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


