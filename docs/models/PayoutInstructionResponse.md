# fireblocks_client.model.payout_instruction_response.PayoutInstructionResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | [**InstructionAmount**](InstructionAmount.md) | [**InstructionAmount**](InstructionAmount.md) |  | 
**state** | [**PayoutInstructionState**](PayoutInstructionState.md) | [**PayoutInstructionState**](PayoutInstructionState.md) |  | 
**payeeAccount** | [**PayeeAccountResponse**](PayeeAccountResponse.md) | [**PayeeAccountResponse**](PayeeAccountResponse.md) |  | 
**[transactions](#transactions)** | list, tuple,  | tuple,  |  | 
**id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

