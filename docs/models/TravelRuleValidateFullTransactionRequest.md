# fireblocks_client.model.travel_rule_validate_full_transaction_request.TravelRuleValidateFullTransactionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[originatorProof](#originatorProof)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Ownership proof related to the originator of the transaction | 
**transactionAsset** | str,  | str,  | The asset involved in the transaction | 
**[originator](#originator)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Information about the originator of the transaction | 
**notificationEmail** | str,  | str,  | The email address where a notification should be sent upon completion of the travel rule | 
**beneficiaryVASPname** | str,  | str,  | The name of the VASP acting as the beneficiary | 
**[pii](#pii)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Personal identifiable information related to the transaction | 
**protocol** | str,  | str,  | The protocol used to perform the travel rule | 
**skipBeneficiaryDataValidation** | bool,  | BoolClass,  | Whether to skip validation of beneficiary data | 
**[beneficiary](#beneficiary)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Information about the beneficiary of the transaction | 
**encrypted** | str,  | str,  | Encrypted data related to the transaction | 
**originatorDid** | str,  | str,  | The DID of the transaction originator | 
**transactionAmount** | str,  | str,  | The amount of the transaction | 
**travelRuleBehavior** | bool,  | BoolClass,  | Whether to check if the transaction is a TRAVEL_RULE in the beneficiary VASP&#x27;s jurisdiction | 
**[transactionBlockchainInfo](#transactionBlockchainInfo)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Information about the blockchain transaction | 
**[beneficiaryProof](#beneficiaryProof)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Ownership proof related to the beneficiary of the transaction | 
**beneficiaryDid** | str,  | str,  | The DID of the transaction beneficiary | 
**originatorVASPdid** | str,  | str,  | The VASP ID of the transaction originator | 
**beneficiaryVASPdid** | str,  | str,  | The VASP ID of the transaction beneficiary | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactionBlockchainInfo

Information about the blockchain transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Information about the blockchain transaction | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TravelRuleTransactionBlockchainInfo](TravelRuleTransactionBlockchainInfo.md) | [**TravelRuleTransactionBlockchainInfo**](TravelRuleTransactionBlockchainInfo.md) | [**TravelRuleTransactionBlockchainInfo**](TravelRuleTransactionBlockchainInfo.md) |  | 

# originator

Information about the originator of the transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Information about the originator of the transaction | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TravelRulePiiIVMS](TravelRulePiiIVMS.md) | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) |  | 

# beneficiary

Information about the beneficiary of the transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Information about the beneficiary of the transaction | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TravelRulePiiIVMS](TravelRulePiiIVMS.md) | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) |  | 

# originatorProof

Ownership proof related to the originator of the transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Ownership proof related to the originator of the transaction | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TravelRuleOwnershipProof](TravelRuleOwnershipProof.md) | [**TravelRuleOwnershipProof**](TravelRuleOwnershipProof.md) | [**TravelRuleOwnershipProof**](TravelRuleOwnershipProof.md) |  | 

# beneficiaryProof

Ownership proof related to the beneficiary of the transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Ownership proof related to the beneficiary of the transaction | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TravelRuleOwnershipProof](TravelRuleOwnershipProof.md) | [**TravelRuleOwnershipProof**](TravelRuleOwnershipProof.md) | [**TravelRuleOwnershipProof**](TravelRuleOwnershipProof.md) |  | 

# pii

Personal identifiable information related to the transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Personal identifiable information related to the transaction | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TravelRulePiiIVMS](TravelRulePiiIVMS.md) | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

