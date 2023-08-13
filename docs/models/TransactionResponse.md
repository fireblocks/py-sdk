# fireblocks_client.model.transaction_response.TransactionResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | ID of the transaction. | [optional] 
**externalTxId** | str,  | str,  | Unique transaction ID provided by the user. Fireblocks highly recommends setting an &#x60;externalTxId&#x60; for every transaction created, to avoid submitting the same transaction twice. | [optional] 
**status** | str,  | str,  | The primary status of the transaction. For details, see [Primary transaction statuses](https://developers.fireblocks.com/reference/primary-transaction-statuses). | [optional] 
**subStatus** | str,  | str,  | See [Transaction substatuses](https://developers.fireblocks.com/reference/transaction-substatuses) for the list of transaction sub statuses. | [optional] 
**txHash** | str,  | str,  | The hash of the transaction on the blockchain.  * This parameter exists if at least one of the following conditions is met:       1. The transaction’s source type is &#x60;UNKNOWN&#x60;, &#x60;WHITELISTED_ADDRESS&#x60;, &#x60;NETWORK_CONNECTION&#x60;, &#x60;ONE_TIME_ADDRESS&#x60;, &#x60;FIAT_ACCOUNT&#x60; or &#x60;GAS_STATION&#x60;.       2. The transaction’s source type is &#x60;VAULT&#x60; and the status is either: &#x60;CONFIRMING&#x60;, &#x60;COMPLETED&#x60;, or was in any of these statuses prior to changing to &#x60;FAILED&#x60; or &#x60;REJECTED&#x60;. In some instances, transactions in status &#x60;BROADCASTING&#x60; will include the txHash as well.       3. The transaction’s source type is &#x60;EXCHANGE_ACCOUNT&#x60; and the transaction’s destination type is &#x60;VAULT&#x60;, and the status is either: &#x60;CONFIRMING&#x60;, &#x60;COMPLETED&#x60;, or was in any of these status prior to changing to &#x60;FAILED&#x60;.   * In addition, the following conditions must be met:      1. The asset is a crypto asset (not fiat).      2. The transaction operation is not RAW or &#x60;TYPED_MESSAGE&#x60;. | [optional] 
**operation** | [**GetTransactionOperation**](GetTransactionOperation.md) | [**GetTransactionOperation**](GetTransactionOperation.md) |  | [optional] 
**note** | str,  | str,  | Custom note, not sent to the blockchain, that describes the transaction at your Fireblocks workspace. | [optional] 
**assetId** | str,  | str,  | The ID of the asset to transfer, for &#x60;TRANSFER&#x60;, &#x60;MINT&#x60;, &#x60;BURN&#x60;, &#x60;ENABLE_ASSET&#x60;,&#x60;STAKE&#x60; ,&#x60;UNSTAKE&#x60; or &#x60;WITHDRAW&#x60; operations. [See the list of supported assets and their IDs on Fireblocks.](https://developers.fireblocks.com/reference/get_supported-assets) | [optional] 
**source** | [**SourceTransferPeerPathResponse**](SourceTransferPeerPathResponse.md) | [**SourceTransferPeerPathResponse**](SourceTransferPeerPathResponse.md) |  | [optional] 
**sourceAddress** | str,  | str,  | For account based assets only, the source address of the transaction. **Note:** If the status is &#x60;CONFIRMING&#x60;, &#x60;COMPLETED&#x60;, or has been &#x60;CONFIRMING&#x60;; then moved forward to &#x60;FAILED&#x60; or &#x60;REJECTED&#x60;, then this parameter will contain the source address. In any other case, this parameter will be empty. | [optional] 
**tag** | str,  | str,  | Source address tag for XRP, used as memo for EOS/XLM, or Bank Transfer Description for the fiat provider BLINC (by BCB Group). | [optional] 
**destination** | [**DestinationTransferPeerPathResponse**](DestinationTransferPeerPathResponse.md) | [**DestinationTransferPeerPathResponse**](DestinationTransferPeerPathResponse.md) |  | [optional] 
**[destinations](#destinations)** | list, tuple,  | tuple,  | The transaction’s destinations. **Note:** In case the transaction is sent to a single destination, the &#x60;destination&#x60; parameter is used instead of this. | [optional] 
**destinationAddress** | str,  | str,  | Address where the asset were transferred. Notes:   - For [Multi destination transactions](https://support.fireblocks.io/hc/en-us/articles/360018447980-Multi-destination-transactions), this parameter will be empty. In this case, you should refer to the destinations field.   - If the status is &#x60;CONFIRMING&#x60;, &#x60;COMPLETED&#x60;, or has been &#x60;CONFIRMING&#x60;; then moved forward to &#x60;FAILED&#x60; or &#x60;REJECTED&#x60;, then this parameter will contain the destination address. In any other case, this parameter will be empty. | [optional] 
**destinationAddressDescription** | str,  | str,  | Description of the address. | [optional] 
**destinationTag** | str,  | str,  | Destination address tag for XRP, used as memo for EOS/XLM, or Bank Transfer Description for the fiat provider BLINC (by BCB Group). | [optional] 
**[contractCallDecodedData](#contractCallDecodedData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Decoded data for &#x60;CONTRACT_CALL&#x60; operations. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for setting this parameter&#x27;s value. | [optional] 
**amountInfo** | [**AmountInfo**](AmountInfo.md) | [**AmountInfo**](AmountInfo.md) |  | [optional] 
**treatAsGrossAmount** | bool,  | BoolClass,  | For transactions initiated via this Fireblocks workspace, when set to &#x60;true&#x60;, the fee is deducted from the requested amount.  **Note**: This parameter can only be considered if a transaction&#x27;s asset is a base asset, such as ETH or MATIC. If the asset can&#x27;t be used for transaction fees, like USDC, this parameter is ignored and the fee is deducted from the relevant base asset wallet in the source account. | [optional] 
**feeInfo** | [**FeeInfo**](FeeInfo.md) | [**FeeInfo**](FeeInfo.md) |  | [optional] 
**feeCurrency** | str,  | str,  | The asset which was withdrawn to pay the transaction fee, for example ETH for EVM-based blockchains, BTC for Tether Omni. | [optional] 
**[networkRecords](#networkRecords)** | list, tuple,  | tuple,  | In case a single transaction resulted with multiple transfers, for example a result of a contract call, then this parameter specifies each transfer that took place on the blockchain. In case of a single transfer transaction, this parameter is empty. | [optional] 
**createdAt** | decimal.Decimal, int, float,  | decimal.Decimal,  | The transaction’s creation date and time, in unix timestamp. | [optional] 
**lastUpdated** | decimal.Decimal, int, float,  | decimal.Decimal,  | The transaction’s last update date and time, in unix timestamp. | [optional] 
**createdBy** | str,  | str,  | User ID of the initiator of the transaction. | [optional] 
**[signedBy](#signedBy)** | list, tuple,  | tuple,  | User ID’s of the signers of the transaction. | [optional] 
**rejectedBy** | str,  | str,  | User ID of the user that rejected the transaction (in case it was rejected). | [optional] 
**authorizationInfo** | [**AuthorizationInfo**](AuthorizationInfo.md) | [**AuthorizationInfo**](AuthorizationInfo.md) |  | [optional] 
**exchangeTxId** | str,  | str,  | If the transaction originated from an exchange, this is the ID of this transaction at the exchange. | [optional] 
**customerRefId** | str,  | str,  | The ID for AML providers to associate the owner of funds with transactions. | [optional] 
**amlScreeningResult** | [**AmlScreeningResult**](AmlScreeningResult.md) | [**AmlScreeningResult**](AmlScreeningResult.md) |  | [optional] 
**[extraParameters](#extraParameters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Additional protocol / operation specific key-value parameters:  For UTXO-based blockchain input selection, add the key &#x60;inputsSelection&#x60; with the value set the [input selection structure.](https://developers.fireblocks.com/reference/transaction-objects#inputsselection) The inputs can be retrieved from the [Retrieve Unspent Inputs endpoint.](https://developers.fireblocks.com/reference/get_vault-accounts-vaultaccountid-assetid-unspent-inputs)  For &#x60;RAW&#x60; operations, add the key &#x60;rawMessageData&#x60; with the value set to the [raw message data structure.](https://developers.fireblocks.com/reference/raw-signing-objects#rawmessagedata)  For &#x60;CONTRACT_CALL&#x60; operations, add the key &#x60;contractCallData&#x60; with the value set to the Ethereum smart contract Application Binary Interface (ABI) payload. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions.  | [optional] 
**signedMessages** | [**SignedMessage**](SignedMessage.md) | [**SignedMessage**](SignedMessage.md) |  | [optional] 
**numOfConfirmations** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of confirmations of the transaction. The number will increase until the transaction will be considered completed according to the confirmation policy. | [optional] 
**blockInfo** | [**BlockInfo**](BlockInfo.md) | [**BlockInfo**](BlockInfo.md) |  | [optional] 
**index** | decimal.Decimal, int, float,  | decimal.Decimal,  | For UTXO based assets this is the vOut, for Ethereum based, this is the index of the event of the contract call.  **Note:** This field is not returned if a transaction uses the &#x60;destinations&#x60; object with more than one value. | [optional] 
**rewardInfo** | [**RewardInfo**](RewardInfo.md) | [**RewardInfo**](RewardInfo.md) |  | [optional] 
**systemMessages** | [**SystemMessageInfo**](SystemMessageInfo.md) | [**SystemMessageInfo**](SystemMessageInfo.md) |  | [optional] 
**addressType** | str,  | str,  |  | [optional] must be one of ["WHITELISTED", "ONE_TIME", ] 
**requestedAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount requested by the user. Deprecated - please use the &#x60;amountInfo&#x60; field for accuracy. | [optional] 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | If the transfer is a withdrawal from an exchange, the actual amount that was requested to be transferred. Otherwise, the requested amount. Deprecated - please use the &#x60;amountInfo&#x60; field for accuracy. | [optional] 
**netAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The net amount of the transaction, after fee deduction. Deprecated - please use the &#x60;amountInfo&#x60; field for accuracy. | [optional] 
**amountUSD** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The USD value of the requested amount. Deprecated - please use the &#x60;amountInfo&#x60; field for accuracy. | [optional] 
**serviceFee** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total fee deducted by the exchange from the actual requested amount (&#x60;serviceFee&#x60; &#x3D; &#x60;amount&#x60; - &#x60;netAmount&#x60;). Deprecated - please use the &#x60;feeInfo&#x60; field for accuracy. | [optional] 
**fee** | decimal.Decimal, int, float,  | decimal.Decimal,  | Deprecated - please use the &#x60;feeInfo&#x60; field for accuracy. | [optional] 
**networkFee** | decimal.Decimal, int, float,  | decimal.Decimal,  | The fee paid to the network. Deprecated - please use the &#x60;feeInfo&#x60; field for accuracy. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# destinations

The transaction’s destinations. **Note:** In case the transaction is sent to a single destination, the `destination` parameter is used instead of this.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The transaction’s destinations. **Note:** In case the transaction is sent to a single destination, the &#x60;destination&#x60; parameter is used instead of this. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionResponseDestination**](TransactionResponseDestination.md) | [**TransactionResponseDestination**](TransactionResponseDestination.md) | [**TransactionResponseDestination**](TransactionResponseDestination.md) |  | 

# contractCallDecodedData

Decoded data for `CONTRACT_CALL` operations. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for setting this parameter's value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Decoded data for &#x60;CONTRACT_CALL&#x60; operations. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for setting this parameter&#x27;s value. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**contractName** | str,  | str,  |  | [optional] 
**[functionCalls](#functionCalls)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# functionCalls

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# networkRecords

In case a single transaction resulted with multiple transfers, for example a result of a contract call, then this parameter specifies each transfer that took place on the blockchain. In case of a single transfer transaction, this parameter is empty.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | In case a single transaction resulted with multiple transfers, for example a result of a contract call, then this parameter specifies each transfer that took place on the blockchain. In case of a single transfer transaction, this parameter is empty. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NetworkRecord**](NetworkRecord.md) | [**NetworkRecord**](NetworkRecord.md) | [**NetworkRecord**](NetworkRecord.md) |  | 

# signedBy

User ID’s of the signers of the transaction.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | User ID’s of the signers of the transaction. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# extraParameters

Additional protocol / operation specific key-value parameters:  For UTXO-based blockchain input selection, add the key `inputsSelection` with the value set the [input selection structure.](https://developers.fireblocks.com/reference/transaction-objects#inputsselection) The inputs can be retrieved from the [Retrieve Unspent Inputs endpoint.](https://developers.fireblocks.com/reference/get_vault-accounts-vaultaccountid-assetid-unspent-inputs)  For `RAW` operations, add the key `rawMessageData` with the value set to the [raw message data structure.](https://developers.fireblocks.com/reference/raw-signing-objects#rawmessagedata)  For `CONTRACT_CALL` operations, add the key `contractCallData` with the value set to the Ethereum smart contract Application Binary Interface (ABI) payload. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Additional protocol / operation specific key-value parameters:  For UTXO-based blockchain input selection, add the key &#x60;inputsSelection&#x60; with the value set the [input selection structure.](https://developers.fireblocks.com/reference/transaction-objects#inputsselection) The inputs can be retrieved from the [Retrieve Unspent Inputs endpoint.](https://developers.fireblocks.com/reference/get_vault-accounts-vaultaccountid-assetid-unspent-inputs)  For &#x60;RAW&#x60; operations, add the key &#x60;rawMessageData&#x60; with the value set to the [raw message data structure.](https://developers.fireblocks.com/reference/raw-signing-objects#rawmessagedata)  For &#x60;CONTRACT_CALL&#x60; operations, add the key &#x60;contractCallData&#x60; with the value set to the Ethereum smart contract Application Binary Interface (ABI) payload. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions.  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

