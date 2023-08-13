# fireblocks_client.model.transaction_request.TransactionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operation** | [**TransactionOperation**](TransactionOperation.md) | [**TransactionOperation**](TransactionOperation.md) |  | [optional] 
**note** | str,  | str,  | Custom note, not sent to the blockchain, to describe the transaction at your Fireblocks workspace. | [optional] 
**externalTxId** | str,  | str,  | An optional but highly recommended parameter. Fireblocks will reject future transactions with same ID.  You should set this to a unique ID representing the transaction, to avoid submitting the same transaction twice. This helps with cases where submitting the transaction responds with an error code due to Internet interruptions, but the transaction was actually sent and processed. To validate whether a transaction has been processed, [Find a specific transaction by external transaction ID](https://developers.fireblocks.com/reference/get_transactions-external-tx-id-externaltxid). There is no specific format required for this parameter. | [optional] 
**assetId** | str,  | str,  | The ID of the asset to transfer, for &#x60;TRANSFER&#x60;, &#x60;MINT&#x60; or &#x60;BURN&#x60; operations. [See the list of supported assets and their IDs on Fireblocks.](https://developers.fireblocks.com/reference/get_supported-assets) | [optional] 
**source** | [**TransferPeerPath**](TransferPeerPath.md) | [**TransferPeerPath**](TransferPeerPath.md) |  | [optional] 
**destination** | [**DestinationTransferPeerPath**](DestinationTransferPeerPath.md) | [**DestinationTransferPeerPath**](DestinationTransferPeerPath.md) |  | [optional] 
**[destinations](#destinations)** | list, tuple,  | tuple,  | For UTXO based blockchains, you can send a single transaction to multiple destinations. | [optional] 
**[amount](#amount)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For &#x60;TRANSFER&#x60; operations, the requested amount to transfer, in the asset’s unit. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. | [optional] 
**treatAsGrossAmount** | bool,  | BoolClass,  | \&quot;When set to &#x60;true&#x60;, the fee will be deducted from the requested amount.\&quot;  **Note**: This parameter can only be considered if a transaction’s asset is a base asset, such as ETH or MATIC. If the asset can’t be used for transaction fees, like USDC, this parameter is ignored and the fee is deducted from the relevant base asset wallet in the source account. | [optional] 
**forceSweep** | bool,  | BoolClass,  | For Polkadot, Kusama and Westend transactions only. When set to true, Fireblocks will empty the asset wallet.     **Note:** If set to true when the source account is exactly 1 DOT, the transaction will fail. Any amount more or less than 1 DOT succeeds. This is a Polkadot blockchain limitation. | [optional] 
**feeLevel** | str,  | str,  | For UTXO or EVM-based blockchains only. Defines the blockchain fee level which will be payed for the transaction. Alternatively, specific fee estimation parameters exist below. | [optional] must be one of ["LOW", "MEDIUM", "HIGH", ] 
**[fee](#fee)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For UTXO-based blockchains, the fee per bytes in the asset’s smallest unit (Satoshi, Latoshi, etc.).  For Ripple, the fee for the transaction. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. | [optional] 
**[priorityFee](#priorityFee)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For Ethereum-based blockchains only, the fee for EIP-1559 transaction pricing mechanism. Value is in Gwei.  Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. | [optional] 
**failOnLowFee** | bool,  | BoolClass,  | When set to &#x60;true&#x60;, in case the current &#x60;MEDIUM&#x60; fee level is higher than the one specified in the transaction, the transaction will fail to avoid getting stuck with no confirmations. | [optional] 
**maxFee** | str,  | str,  | The maximum fee (gas price or fee per byte) that should be payed for the transaction.  In case the current value of the requested &#x60;feeLevel&#x60; is higher than this requested maximum fee.  Represented by a numeric string for accurate precision. | [optional] 
**[gasLimit](#gasLimit)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For EVM-based blockchains only. Units of gas required to process the transaction. Note: Only two of the three arguments can be specified in a single transaction: &#x60;gasLimit&#x60;, &#x60;gasPrice&#x60; and &#x60;networkFee&#x60;. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. | [optional] 
**[gasPrice](#gasPrice)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For non-EIP-1559, EVM-based transactions. Price per gas unit (in Ethereum this is specified in Gwei).  Note: Only two of the three arguments can be specified in a single transaction: &#x60;gasLimit&#x60;, &#x60;gasPrice&#x60; and &#x60;networkFee&#x60;. Fireblocks recommends using a numeric string for accurate precision.  Although a number input exists, it is deprecated. | [optional] 
**[networkFee](#networkFee)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For EVM-based blockchains only. The total transaction fee in the blockchain’s largest unit. Note: Only two of the three arguments can be specified in a single transaction: &#x60;gasLimit&#x60;, &#x60;gasPrice&#x60; and &#x60;networkFee&#x60;. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. - The transaction blockchain fee. - For Ethereum, you can&#x27;t pass gasPrice, gasLimit and networkFee all together. - A numeric value representation is required. | [optional] 
**replaceTxByHash** | str,  | str,  | For EVM-based blockchains only. In case a transaction is stuck, specify the hash of the stuck transaction to replace it by this transaction with a higher fee, or to replace it with this transaction with a zero fee and drop it from the blockchain. | [optional] 
**[extraParameters](#extraParameters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Additional protocol / operation specific key-value parameters:  For UTXO-based blockchain input selection, add the key &#x60;inputsSelection&#x60; with the value set the [input selection structure.](https://developers.fireblocks.com/reference/transaction-objects#inputsselection) The inputs can be retrieved from the [Retrieve Unspent Inputs endpoint.](https://developers.fireblocks.com/reference/get_vault-accounts-vaultaccountid-assetid-unspent-inputs)  For &#x60;RAW&#x60; operations, add the key &#x60;rawMessageData&#x60; with the value set to the [raw message data structure.](https://developers.fireblocks.com/reference/raw-signing-objects#rawmessagedata)  For &#x60;CONTRACT_CALL&#x60; operations, add the key &#x60;contractCallData&#x60; with the value set to the Ethereum smart contract Application Binary Interface (ABI) payload. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions.  | [optional] 
**customerRefId** | str,  | str,  | The ID for AML providers to associate the owner of funds with transactions. | [optional] 
**autoStaking** | bool,  | BoolClass,  | This feature is no longer supported. | [optional] 
**[networkStaking](#networkStaking)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This feature is no longer supported. | [optional] 
**[cpuStaking](#cpuStaking)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This feature is no longer supported. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# destinations

For UTXO based blockchains, you can send a single transaction to multiple destinations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | For UTXO based blockchains, you can send a single transaction to multiple destinations. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionRequestDestination**](TransactionRequestDestination.md) | [**TransactionRequestDestination**](TransactionRequestDestination.md) | [**TransactionRequestDestination**](TransactionRequestDestination.md) |  | 

# amount

For `TRANSFER` operations, the requested amount to transfer, in the asset’s unit. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For &#x60;TRANSFER&#x60; operations, the requested amount to transfer, in the asset’s unit. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  | Numeric string (recommended) | 
[one_of_1](#one_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# one_of_0

Numeric string (recommended)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Numeric string (recommended) | 

# one_of_1

Number (deprecated)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# fee

For UTXO-based blockchains, the fee per bytes in the asset’s smallest unit (Satoshi, Latoshi, etc.).  For Ripple, the fee for the transaction. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For UTXO-based blockchains, the fee per bytes in the asset’s smallest unit (Satoshi, Latoshi, etc.).  For Ripple, the fee for the transaction. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  | Numeric string (recommended) | 
[one_of_1](#one_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# one_of_0

Numeric string (recommended)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Numeric string (recommended) | 

# one_of_1

Number (deprecated)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# priorityFee

For Ethereum-based blockchains only, the fee for EIP-1559 transaction pricing mechanism. Value is in Gwei.  Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For Ethereum-based blockchains only, the fee for EIP-1559 transaction pricing mechanism. Value is in Gwei.  Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  | Numeric string (recommended) | 
[one_of_1](#one_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# one_of_0

Numeric string (recommended)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Numeric string (recommended) | 

# one_of_1

Number (deprecated)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# gasLimit

For EVM-based blockchains only. Units of gas required to process the transaction. Note: Only two of the three arguments can be specified in a single transaction: `gasLimit`, `gasPrice` and `networkFee`. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For EVM-based blockchains only. Units of gas required to process the transaction. Note: Only two of the three arguments can be specified in a single transaction: &#x60;gasLimit&#x60;, &#x60;gasPrice&#x60; and &#x60;networkFee&#x60;. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  | Numeric string (recommended) | 
[one_of_1](#one_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# one_of_0

Numeric string (recommended)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Numeric string (recommended) | 

# one_of_1

Number (deprecated)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# gasPrice

For non-EIP-1559, EVM-based transactions. Price per gas unit (in Ethereum this is specified in Gwei).  Note: Only two of the three arguments can be specified in a single transaction: `gasLimit`, `gasPrice` and `networkFee`. Fireblocks recommends using a numeric string for accurate precision.  Although a number input exists, it is deprecated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For non-EIP-1559, EVM-based transactions. Price per gas unit (in Ethereum this is specified in Gwei).  Note: Only two of the three arguments can be specified in a single transaction: &#x60;gasLimit&#x60;, &#x60;gasPrice&#x60; and &#x60;networkFee&#x60;. Fireblocks recommends using a numeric string for accurate precision.  Although a number input exists, it is deprecated. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  | Numeric string (recommended) | 
[one_of_1](#one_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# one_of_0

Numeric string (recommended)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Numeric string (recommended) | 

# one_of_1

Number (deprecated)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# networkFee

For EVM-based blockchains only. The total transaction fee in the blockchain’s largest unit. Note: Only two of the three arguments can be specified in a single transaction: `gasLimit`, `gasPrice` and `networkFee`. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. - The transaction blockchain fee. - For Ethereum, you can't pass gasPrice, gasLimit and networkFee all together. - A numeric value representation is required.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | For EVM-based blockchains only. The total transaction fee in the blockchain’s largest unit. Note: Only two of the three arguments can be specified in a single transaction: &#x60;gasLimit&#x60;, &#x60;gasPrice&#x60; and &#x60;networkFee&#x60;. Fireblocks recommends using a numeric string for accurate precision. Although a number input exists, it is deprecated. - The transaction blockchain fee. - For Ethereum, you can&#x27;t pass gasPrice, gasLimit and networkFee all together. - A numeric value representation is required. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  | Numeric string (recommended) | 
[one_of_1](#one_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# one_of_0

Numeric string (recommended)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Numeric string (recommended) | 

# one_of_1

Number (deprecated)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# extraParameters

Additional protocol / operation specific key-value parameters:  For UTXO-based blockchain input selection, add the key `inputsSelection` with the value set the [input selection structure.](https://developers.fireblocks.com/reference/transaction-objects#inputsselection) The inputs can be retrieved from the [Retrieve Unspent Inputs endpoint.](https://developers.fireblocks.com/reference/get_vault-accounts-vaultaccountid-assetid-unspent-inputs)  For `RAW` operations, add the key `rawMessageData` with the value set to the [raw message data structure.](https://developers.fireblocks.com/reference/raw-signing-objects#rawmessagedata)  For `CONTRACT_CALL` operations, add the key `contractCallData` with the value set to the Ethereum smart contract Application Binary Interface (ABI) payload. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Additional protocol / operation specific key-value parameters:  For UTXO-based blockchain input selection, add the key &#x60;inputsSelection&#x60; with the value set the [input selection structure.](https://developers.fireblocks.com/reference/transaction-objects#inputsselection) The inputs can be retrieved from the [Retrieve Unspent Inputs endpoint.](https://developers.fireblocks.com/reference/get_vault-accounts-vaultaccountid-assetid-unspent-inputs)  For &#x60;RAW&#x60; operations, add the key &#x60;rawMessageData&#x60; with the value set to the [raw message data structure.](https://developers.fireblocks.com/reference/raw-signing-objects#rawmessagedata)  For &#x60;CONTRACT_CALL&#x60; operations, add the key &#x60;contractCallData&#x60; with the value set to the Ethereum smart contract Application Binary Interface (ABI) payload. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions.  | 

# networkStaking

This feature is no longer supported.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This feature is no longer supported. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  | Numeric string (recommended) | 
[one_of_1](#one_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# one_of_0

Numeric string (recommended)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Numeric string (recommended) | 

# one_of_1

Number (deprecated)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# cpuStaking

This feature is no longer supported.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This feature is no longer supported. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  | Numeric string (recommended) | 
[one_of_1](#one_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

# one_of_0

Numeric string (recommended)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Numeric string (recommended) | 

# one_of_1

Number (deprecated)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Number (deprecated) | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

