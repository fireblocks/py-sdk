# fireblocks_client.model.policy_rule_check_result.PolicyRuleCheckResult

The rule validation result

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The rule validation result | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | decimal.Decimal, int, float,  | decimal.Decimal,  | Rule index number in the policy | 
**[errors](#errors)** | list, tuple,  | tuple,  | A set of rule validation error objects | 
**status** | str,  | str,  | Validation status | must be one of ["ok", "failure", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

A set of rule validation error objects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A set of rule validation error objects | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PolicyRuleError**](PolicyRuleError.md) | [**PolicyRuleError**](PolicyRuleError.md) | [**PolicyRuleError**](PolicyRuleError.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

