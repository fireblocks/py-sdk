# fireblocks_client.model.travel_rule_validate_transaction_request.TravelRuleValidateTransactionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**beneficiaryVASPname** | str,  | str,  | Beneficiary VASP name | 
**originatorEqualsBeneficiary** | bool,  | BoolClass,  | \&quot;True\&quot; if the originator and beneficiary is the same person and you therefore do not need to collect any information. \&quot;False\&quot; if it is a third-party transfer. | 
**transactionAsset** | str,  | str,  | Transaction asset symbol BTC,ETH) | 
**beneficiaryAccountNumber** | str,  | str,  | Beneficiary  name | 
**beneficiaryName** | str,  | str,  | Beneficiary  name | 
**transactionAmount** | str,  | str,  | Transaction amount in the transaction asset | 
**travelRuleBehavior** | bool,  | BoolClass,  | This will also check if the transaction is a TRAVEL_RULE in the beneficiary VASP&#x27;s jurisdiction | 
**destination** | str,  | str,  | Transaction destination address | 
**[beneficiaryAddress](#beneficiaryAddress)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Beneficiary  name | 
**originatorVASPdid** | str,  | str,  | This is the identifier assigned to your VASP | 
**beneficiaryVASPdid** | str,  | str,  | This is the identifier assigned to the VASP the funds are being sent to | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# beneficiaryAddress

Beneficiary  name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Beneficiary  name | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TravelRuleAddress](TravelRuleAddress.md) | [**TravelRuleAddress**](TravelRuleAddress.md) | [**TravelRuleAddress**](TravelRuleAddress.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

