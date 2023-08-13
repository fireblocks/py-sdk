# fireblocks_client.model.publish_result.PublishResult

Response object of the publish policy operation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response object of the publish policy operation | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metadata** | [**PolicyMetadata**](PolicyMetadata.md) | [**PolicyMetadata**](PolicyMetadata.md) |  | 
**[rules](#rules)** | list, tuple,  | tuple,  |  | 
**checkResult** | [**PolicyCheckResult**](PolicyCheckResult.md) | [**PolicyCheckResult**](PolicyCheckResult.md) |  | 
**status** | [**PolicyStatus**](PolicyStatus.md) | [**PolicyStatus**](PolicyStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PolicyRule**](PolicyRule.md) | [**PolicyRule**](PolicyRule.md) | [**PolicyRule**](PolicyRule.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

