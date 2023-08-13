# fireblocks_client.model.create_connection_request.CreateConnectionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vaultAccountId** | decimal.Decimal, int, float,  | decimal.Decimal,  | The ID of the vault to connect to the Web3 connection. | 
**[chainIds](#chainIds)** | list, tuple,  | tuple,  | The ID of the blockchain network used in the Web3 connection. | 
**feeLevel** | str,  | str,  | The default fee level. Valid values are &#x60;MEDIUM&#x60; and &#x60;HIGH&#x60;. | must be one of ["MEDIUM", "HIGH", ] 
**uri** | str,  | str,  | The WalletConnect uri provided by the dapp. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# chainIds

The ID of the blockchain network used in the Web3 connection.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The ID of the blockchain network used in the Web3 connection. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

