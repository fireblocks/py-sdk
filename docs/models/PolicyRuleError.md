# fireblocks_client.model.policy_rule_error.PolicyRuleError

Rule validation result error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Rule validation result error | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCodeName** | str,  | str,  | error code name | 
**errorField** | str,  | str,  | The field which the error relates to * operator - transaction initiator * operators - transaction initiators * authorizationGroups - transaction authorizer groups * designatedSigner - transaction signer * designatedSigners - transaction signers * contractMethods - contract methods * amountAggregation - transaction amount aggregation configuration * src - transaction source asset configuration * dst - transaction destination asset configuration  | must be one of ["operator", "operators", "authorizationGroups", "designatedSigner", "designatedSigners", "contractMethods", "amountAggregation", "src", "dst", ] 
**errorMessage** | str,  | str,  | Error message | 
**errorCode** | decimal.Decimal, int, float,  | decimal.Decimal,  | error code | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

