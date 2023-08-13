# fireblocks_client.model.create_transaction_response.CreateTransactionResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The ID of the transaction. | [optional] 
**status** | str,  | str,  | The primary status of the transaction. For details, see [Primary transaction statuses.] (https://developers.fireblocks.com/reference/primary-transaction-statuses) | [optional] 
**systemMessages** | [**SystemMessageInfo**](SystemMessageInfo.md) | [**SystemMessageInfo**](SystemMessageInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

