# fireblocks_client.model.draft_response.DraftResponse

Response object for draft operations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response object for draft operations | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**draftId** | str,  | str,  | Draft unique id | 
**metadata** | [**PolicyMetadata**](PolicyMetadata.md) | [**PolicyMetadata**](PolicyMetadata.md) |  | 
**[rules](#rules)** | list, tuple,  | tuple,  | Draft rules | 
**status** | str,  | str,  | Operation status | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rules

Draft rules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Draft rules | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PolicyRule**](PolicyRule.md) | [**PolicyRule**](PolicyRule.md) | [**PolicyRule**](PolicyRule.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

