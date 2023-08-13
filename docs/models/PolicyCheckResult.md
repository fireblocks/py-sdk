# fireblocks_client.model.policy_check_result.PolicyCheckResult

Policy rules validation result

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Policy rules validation result | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[result](#result)** | list, tuple,  | tuple,  | A set of validation results | 
**errors** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of errors | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# result

A set of validation results

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A set of validation results | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PolicyRuleCheckResult**](PolicyRuleCheckResult.md) | [**PolicyRuleCheckResult**](PolicyRuleCheckResult.md) | [**PolicyRuleCheckResult**](PolicyRuleCheckResult.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

