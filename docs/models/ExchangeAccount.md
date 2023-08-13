# fireblocks_client.model.exchange_account.ExchangeAccount

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**type** | [**ExchangeType**](ExchangeType.md) | [**ExchangeType**](ExchangeType.md) |  | [optional] 
**name** | str,  | str,  | Display name of the exchange account | [optional] 
**status** | str,  | str,  |  | [optional] 
**[assets](#assets)** | list, tuple,  | tuple,  |  | [optional] 
**[tradingAccounts](#tradingAccounts)** | list, tuple,  | tuple,  |  | [optional] 
**isSubaccount** | bool,  | BoolClass,  | True if the account is a subaccount in an exchange | [optional] 
**mainAccountId** | str,  | str,  | if the account is a sub-account, the ID of the main account | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# assets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ExchangeAsset**](ExchangeAsset.md) | [**ExchangeAsset**](ExchangeAsset.md) | [**ExchangeAsset**](ExchangeAsset.md) |  | 

# tradingAccounts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ExchangeTradingAccount**](ExchangeTradingAccount.md) | [**ExchangeTradingAccount**](ExchangeTradingAccount.md) | [**ExchangeTradingAccount**](ExchangeTradingAccount.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

