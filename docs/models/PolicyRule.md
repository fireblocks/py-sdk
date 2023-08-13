# fireblocks_client.model.policy_rule.PolicyRule

Policy rule which is enforced on transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Policy rule which is enforced on transactions | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**externalDescriptor** | str,  | str,  | A unique id identifying the rule | 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Defines the value a transaction must exceed for the rule to apply to it (according to the amountCurrency field) | 
**periodSec** | decimal.Decimal, int, float,  | decimal.Decimal,  | Time period in seconds applied by the amountScope field to accumulate transferred amounts in transactions that match the rule, until the total exceeds the value you specify under Minimum. When the specified amount is reached within that period, whether by one or many transactions, further transactions in that period either fail or require more approvals.  | 
**action** | str,  | str,  | Defines what occurs when a transaction meets the rule&#x27;s criteria * ALLOW - The transaction goes through and can be signed without requiring additional approvals * BLOCK - The transaction is automatically blocked * 2-TIER - Only these users or user groups can approve             If any of them reject the transaction before the required approval threshold is met, the transaction doesn&#x27;t go through            The list of entities are set is \&quot;authorizationGroups\&quot; field  | must be one of ["ALLOW", "BLOCK", "2-TIER", ] 
**asset** | str,  | str,  | Defines the type of asset being transacted, options are * \&quot;*\&quot; - All assets * Specific asset  | 
**type** | str,  | str,  | Policy rule type | must be one of ["TRANSFER", ] 
**amountScope** | str,  | str,  | * SINGLE_TX - limit applies to a single transaction * TIMEFRAME - limit applies to all transactions within the defined time period  | must be one of ["SINGLE_TX", "TIMEFRAME", ] 
**amountCurrency** | str,  | str,  | * USD - Limits the amount of any asset users can transfer based on the USD equivalent of the asset. * EUR - Limits the amount of any asset users can transfer based on the EURO equivalent of the asset. * NATIVE - Limits the amount of an asset a user can transfer when using a specific asset.  | must be one of ["USD", "EUR", "NATIVE", ] 
**operator** | str,  | str,  | (deprecated - replaced by \&quot;operators\&quot;)  | Defines users who can initiate the type of transaction to which the rule applies. options are * \&quot;*\&quot; - All users are allowed * Specific User id | [optional] 
**[operators](#operators)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines users/groups who can initiate the type of transaction to which the rule applies. | [optional] 
**transactionType** | str,  | str,  | Defines the type of transaction to which the rule applies.   * TRANSFER - Default. Transfers funds from one account to another   * CONTRACT_CALL - Calls a smart contract, mainly for DeFi operations.   * APPROVE - Allows a smart contract to withdraw from a designated wallet.   * MINT - Perform a mint operation (increase supply) on a supported token   * BURN - Perform a burn operation (reduce supply) on a supported token   * SUPPLY - Use for DeFi to lend assets   * REDEEM - Use for DeFi to get lending back   * STAKE - Allows you to allocate and lock certain assets for earning staking rewards.   * RAW - An off-chain message with no predefined format, use it to sign any message with your private key.   * TYPED_MESSAGE - An off-chain message type that follows a predefined format, used to sign specific messages that are not actual transactions.  | [optional] must be one of ["TRANSFER", "CONTRACT_CALL", "APPROVE", "MINT", "BURN", "SUPPLY", "REDEEM", "STAKE", "RAW", "TYPED_MESSAGE", ] 
**designatedSigner** | str,  | str,  | (deprecated - replaced by \&quot;designatedSigners\&quot;) Id representing the user who signs transactions that match a specific rule | [optional] 
**[designatedSigners](#designatedSigners)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Set of ids representing the users who signs transactions that match a specific rule | [optional] 
**[srcType](#srcType)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;src\&quot;) source account type | [optional] 
**[srcSubType](#srcSubType)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;src\&quot;) source sub account type | [optional] 
**[srcId](#srcId)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;src\&quot;) source account id | [optional] 
**[src](#src)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines source accounts the rule allows transfers to originate from | [optional] 
**[dstType](#dstType)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;dst\&quot;) destination account type | [optional] 
**[dstSubType](#dstSubType)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;dst\&quot;) destination sub account type | [optional] 
**[dstId](#dstId)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;dst\&quot;) destination account id | [optional] 
**[dst](#dst)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the destination accounts the rule allows transfers to | [optional] 
**dstAddressType** | str,  | str,  | Defines whether the destination to which you are sending funds must be whitelisted, to allow one-time transfers to non-whitelisted external addresses, or both. By default, you can only transfer to an external address after it’s whitelisted.   * WHITELISTED - Can only be sent to whitelisted addresses.   * ONE_TIME - Can only be sent to non-whitelisted external addresses.   * \&quot;*\&quot; - can be sent to whitelisted addresses or non-whitelisted external  | [optional] must be one of ["WHITELISTED", "ONE_TIME", "*", ] 
**[authorizers](#authorizers)** | list, tuple,  | tuple,  | (deprecated - replaced by \&quot;authorizationGroups\&quot;) Allowed entities which can approves a transaction | [optional] 
**authorizersCount** | decimal.Decimal, int, float,  | decimal.Decimal,  | (deprecated - replaced by \&quot;authorizationGroups\&quot;) Min amount of entities which are needed to approve a transaction | [optional] 
**[authorizationGroups](#authorizationGroups)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the transaction approval terms | [optional] 
**[amountAggregation](#amountAggregation)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the method by which the Policy Engine calculates accumulation. It uses the Initiator, Source, and Destination to calculate accumulation toward the value under Minimum, for the time under Time Period.  | [optional] 
**[rawMessageSigning](#rawMessageSigning)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Raw message signing configuration | [optional] 
**applyForApprove** | bool,  | BoolClass,  | Applying this rule over APPROVE type transactions (can only be enabled when rule&#x27;s transaction type is TRANSFER) | [optional] 
**applyForTypedMessage** | bool,  | BoolClass,  | Applying this rule over TYPED_MESSAGE type transactions (can only be enabled when rule&#x27;s transaction type is CONTRACT_CALL) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# operators

Defines users/groups who can initiate the type of transaction to which the rule applies.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines users/groups who can initiate the type of transaction to which the rule applies. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wildcard** | str,  | str,  | If used then this property should appear as the only child property * \&quot;*\&quot; - All users are allowed  | [optional] must be one of ["*", ] 
**[users](#users)** | list, tuple,  | tuple,  | Set of users ids | [optional] 
**[usersGroups](#usersGroups)** | list, tuple,  | tuple,  | Set of group ids | [optional] 
**[services](#services)** | list, tuple,  | tuple,  | set of services to initiate transactions | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# users

Set of users ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Set of users ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# usersGroups

Set of group ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Set of group ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# services

set of services to initiate transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | set of services to initiate transactions | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# designatedSigners

Set of ids representing the users who signs transactions that match a specific rule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Set of ids representing the users who signs transactions that match a specific rule | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[users](#users)** | list, tuple,  | tuple,  | Set of users ids | [optional] 
**[usersGroups](#usersGroups)** | list, tuple,  | tuple,  | Set of group ids | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# users

Set of users ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Set of users ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# usersGroups

Set of group ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Set of group ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# srcType

(deprecated - replaced by \"src\") source account type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;src\&quot;) source account type | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[PolicySrcOrDestType](PolicySrcOrDestType.md) | [**PolicySrcOrDestType**](PolicySrcOrDestType.md) | [**PolicySrcOrDestType**](PolicySrcOrDestType.md) |  | 

# srcSubType

(deprecated - replaced by \"src\") source sub account type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;src\&quot;) source sub account type | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[PolicySrcOrDestSubType](PolicySrcOrDestSubType.md) | [**PolicySrcOrDestSubType**](PolicySrcOrDestSubType.md) | [**PolicySrcOrDestSubType**](PolicySrcOrDestSubType.md) |  | 

# srcId

(deprecated - replaced by \"src\") source account id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;src\&quot;) source account id | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | str,  | str,  | Defines the account id, options are * \&quot;*\&quot; - All accounts * Specific account id  | 

# all_of_0

Defines the account id, options are * \"*\" - All accounts * Specific account id 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Defines the account id, options are * \&quot;*\&quot; - All accounts * Specific account id  | 

# src

Defines source accounts the rule allows transfers to originate from

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines source accounts the rule allows transfers to originate from | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[ids](#ids)** | list, tuple,  | tuple,  | A set of ids | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ids

A set of ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A set of ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  | A set of ids in a tuple format | 

# items

A set of ids in a tuple format

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A set of ids in a tuple format | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  | Defines the account id, options are * \&quot;*\&quot; - All accounts * Specific account id  | 
[PolicySrcOrDestType](PolicySrcOrDestType.md) | [**PolicySrcOrDestType**](PolicySrcOrDestType.md) | [**PolicySrcOrDestType**](PolicySrcOrDestType.md) |  | 
[PolicySrcOrDestSubType](PolicySrcOrDestSubType.md) | [**PolicySrcOrDestSubType**](PolicySrcOrDestSubType.md) | [**PolicySrcOrDestSubType**](PolicySrcOrDestSubType.md) |  | 

# one_of_0

Defines the account id, options are * \"*\" - All accounts * Specific account id 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Defines the account id, options are * \&quot;*\&quot; - All accounts * Specific account id  | 

# dstType

(deprecated - replaced by \"dst\") destination account type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;dst\&quot;) destination account type | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[PolicySrcOrDestType](PolicySrcOrDestType.md) | [**PolicySrcOrDestType**](PolicySrcOrDestType.md) | [**PolicySrcOrDestType**](PolicySrcOrDestType.md) |  | 

# dstSubType

(deprecated - replaced by \"dst\") destination sub account type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;dst\&quot;) destination sub account type | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[PolicySrcOrDestSubType](PolicySrcOrDestSubType.md) | [**PolicySrcOrDestSubType**](PolicySrcOrDestSubType.md) | [**PolicySrcOrDestSubType**](PolicySrcOrDestSubType.md) |  | 

# dstId

(deprecated - replaced by \"dst\") destination account id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | (deprecated - replaced by \&quot;dst\&quot;) destination account id | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | str,  | str,  | Defines the account id, options are * \&quot;*\&quot; - All accounts * Specific account id  | 

# all_of_0

Defines the account id, options are * \"*\" - All accounts * Specific account id 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Defines the account id, options are * \&quot;*\&quot; - All accounts * Specific account id  | 

# dst

Defines the destination accounts the rule allows transfers to

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the destination accounts the rule allows transfers to | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[ids](#ids)** | list, tuple,  | tuple,  | A set of ids | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ids

A set of ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A set of ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  | A set of ids in a tuple format | 

# items

A set of ids in a tuple format

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A set of ids in a tuple format | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  | Defines the account id, options are * \&quot;*\&quot; - All accounts * Specific account id  | 
[PolicySrcOrDestType](PolicySrcOrDestType.md) | [**PolicySrcOrDestType**](PolicySrcOrDestType.md) | [**PolicySrcOrDestType**](PolicySrcOrDestType.md) |  | 
[PolicySrcOrDestSubType](PolicySrcOrDestSubType.md) | [**PolicySrcOrDestSubType**](PolicySrcOrDestSubType.md) | [**PolicySrcOrDestSubType**](PolicySrcOrDestSubType.md) |  | 

# one_of_0

Defines the account id, options are * \"*\" - All accounts * Specific account id 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Defines the account id, options are * \&quot;*\&quot; - All accounts * Specific account id  | 

# authorizers

(deprecated - replaced by \"authorizationGroups\") Allowed entities which can approves a transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | (deprecated - replaced by \&quot;authorizationGroups\&quot;) Allowed entities which can approves a transaction | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# authorizationGroups

Defines the transaction approval terms

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the transaction approval terms | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**logic** | str,  | str,  | * AND - requires approval of all authorization groups * OR - requires approval of at least one of the authorization groups  | [optional] must be one of ["AND", "OR", ] 
**allowOperatorAsAuthorizer** | bool,  | BoolClass,  | Defines whether the user who initiates a transaction can approve their own transaction and count toward the approval threshold for their transaction | [optional] 
**[groups](#groups)** | list, tuple,  | tuple,  | Groups of entities which can approve the transaction | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# groups

Groups of entities which can approve the transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Groups of entities which can approve the transaction | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[users](#users)** | list, tuple,  | tuple,  | User ids | [optional] 
**[usersGroups](#usersGroups)** | list, tuple,  | tuple,  | Group ids | [optional] 
**th** | decimal.Decimal, int, float,  | decimal.Decimal,  | Represents the min amount of entities which are required to approve the transaction, default is 1. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# users

User ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | User ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# usersGroups

Group ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Group ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# amountAggregation

Defines the method by which the Policy Engine calculates accumulation. It uses the Initiator, Source, and Destination to calculate accumulation toward the value under Minimum, for the time under Time Period. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the method by which the Policy Engine calculates accumulation. It uses the Initiator, Source, and Destination to calculate accumulation toward the value under Minimum, for the time under Time Period.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operators** | [**AmountAggregationTimePeriodMethod**](AmountAggregationTimePeriodMethod.md) | [**AmountAggregationTimePeriodMethod**](AmountAggregationTimePeriodMethod.md) |  | [optional] 
**srcTransferPeers** | [**AmountAggregationTimePeriodMethod**](AmountAggregationTimePeriodMethod.md) | [**AmountAggregationTimePeriodMethod**](AmountAggregationTimePeriodMethod.md) |  | [optional] 
**dstTransferPeers** | [**AmountAggregationTimePeriodMethod**](AmountAggregationTimePeriodMethod.md) | [**AmountAggregationTimePeriodMethod**](AmountAggregationTimePeriodMethod.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rawMessageSigning

Raw message signing configuration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Raw message signing configuration | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**algorithm** | str,  | str,  |  | [optional] 
**[derivationPath](#derivationPath)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# derivationPath

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[path](#path)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# path

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

