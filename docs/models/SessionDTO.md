# fireblocks_client.model.session_dto.SessionDTO

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vaultAccountId** | decimal.Decimal, int, float,  | decimal.Decimal,  | The vault to connect | 
**[chainIds](#chainIds)** | list, tuple,  | tuple,  | The chains approved for the connection | 
**[sessionMetadata](#sessionMetadata)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Metadata of the connection (provided by the dapp) | 
**feeLevel** | str,  | str,  | The default fee level | must be one of ["MEDIUM", "HIGH", ] 
**id** | str,  | str,  | Id of the connection | 
**creationDate** | str, datetime,  | str,  | Timestamp of the session&#x27;s creation | value must conform to RFC-3339 date-time
**connectionType** | str,  | str,  | The connection&#x27;s type | must be one of ["WalletConnect", ] 
**userId** | str,  | str,  | Id of the user that created the connection | 
**connectionMethod** | str,  | str,  | The method through which the connection was established | must be one of ["DESKTOP", "MOBILE", "API", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sessionMetadata

Metadata of the connection (provided by the dapp)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Metadata of the connection (provided by the dapp) | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[SessionMetadata](SessionMetadata.md) | [**SessionMetadata**](SessionMetadata.md) | [**SessionMetadata**](SessionMetadata.md) |  | 

# chainIds

The chains approved for the connection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The chains approved for the connection | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

