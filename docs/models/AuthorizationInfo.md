# fireblocks_client.model.authorization_info.AuthorizationInfo

The information about your [Transaction Authorization Policy (TAP).](https://developers.fireblocks.com/docs/capabilities#transaction-authorization-policy-tap)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The information about your [Transaction Authorization Policy (TAP).](https://developers.fireblocks.com/docs/capabilities#transaction-authorization-policy-tap) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**allowOperatorAsAuthorizer** | bool,  | BoolClass,  |  | [optional] 
**logic** | str,  | str,  |  | [optional] must be one of ["AND", "OR", ] 
**[groups](#groups)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# groups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AuthorizationGroups**](AuthorizationGroups.md) | [**AuthorizationGroups**](AuthorizationGroups.md) | [**AuthorizationGroups**](AuthorizationGroups.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

