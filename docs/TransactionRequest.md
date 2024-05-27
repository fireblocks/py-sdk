# TransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**TransactionOperation**](TransactionOperation.md) |  | [optional] 
**note** | **str** | Custom note, not sent to the blockchain, to describe the transaction at your Fireblocks workspace. | [optional] 
**external_tx_id** | **str** | An optional but highly recommended parameter. Fireblocks will reject future transactions with same ID.  You should set this to a unique ID representing the transaction, to avoid submitting the same transaction twice. This helps with cases where submitting the transaction responds with an error code due to Internet interruptions, but the transaction was actually sent and processed. To validate whether a transaction has been processed, [Find a specific transaction by external transaction ID](https://developers.fireblocks.com/reference/get_transactions-external-tx-id-externaltxid). There is no specific format required for this parameter. | [optional] 
**asset_id** | **str** | The ID of the asset to transfer, for &#x60;TRANSFER&#x60;, &#x60;MINT&#x60; or &#x60;BURN&#x60; operations. [See the list of supported assets and their IDs on Fireblocks.](https://developers.fireblocks.com/reference/get_supported-assets) | [optional] 
**source** | [**SourceTransferPeerPath**](SourceTransferPeerPath.md) |  | [optional] 
**destination** | [**DestinationTransferPeerPath**](DestinationTransferPeerPath.md) |  | [optional] 
**destinations** | [**List[TransactionRequestDestination]**](TransactionRequestDestination.md) | For UTXO based blockchains, you can send a single transaction to multiple destinations. | [optional] 
**amount** | [**TransactionRequestAmount**](TransactionRequestAmount.md) |  | [optional] 
**treat_as_gross_amount** | **bool** | \&quot;When set to &#x60;true&#x60;, the fee will be deducted from the requested amount.\&quot;  **Note**: This parameter can only be considered if a transaction’s asset is a base asset, such as ETH or MATIC. If the asset can’t be used for transaction fees, like USDC, this parameter is ignored and the fee is deducted from the relevant base asset wallet in the source account. | [optional] 
**force_sweep** | **bool** | For Polkadot, Kusama and Westend transactions only. When set to true, Fireblocks will empty the asset wallet.     **Note:** If set to true when the source account is exactly 1 DOT, the transaction will fail. Any amount more or less than 1 DOT succeeds. This is a Polkadot blockchain limitation. | [optional] 
**fee_level** | **str** | For UTXO or EVM-based blockchains only. Defines the blockchain fee level which will be payed for the transaction. Alternatively, specific fee estimation parameters exist below. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 
**priority_fee** | [**TransactionRequestPriorityFee**](TransactionRequestPriorityFee.md) |  | [optional] 
**fail_on_low_fee** | **bool** | When set to &#x60;true&#x60;, in case the current &#x60;MEDIUM&#x60; fee level is higher than the one specified in the transaction, the transaction will fail to avoid getting stuck with no confirmations. | [optional] 
**max_fee** | **str** | The maximum fee (gas price or fee per byte) that should be payed for the transaction.  In case the current value of the requested &#x60;feeLevel&#x60; is higher than this requested maximum fee.  Represented by a numeric string for accurate precision. | [optional] 
**gas_limit** | [**TransactionRequestGasLimit**](TransactionRequestGasLimit.md) |  | [optional] 
**gas_price** | [**TransactionRequestGasPrice**](TransactionRequestGasPrice.md) |  | [optional] 
**network_fee** | [**TransactionRequestNetworkFee**](TransactionRequestNetworkFee.md) |  | [optional] 
**replace_tx_by_hash** | **str** | For EVM-based blockchains only. In case a transaction is stuck, specify the hash of the stuck transaction to replace it by this transaction with a higher fee, or to replace it with this transaction with a zero fee and drop it from the blockchain. | [optional] 
**extra_parameters** | **object** | Additional protocol / operation specific key-value parameters:  For UTXO-based blockchain input selection, add the key &#x60;inputsSelection&#x60; with the value set the [input selection structure.](https://developers.fireblocks.com/reference/transaction-objects#inputsselection) The inputs can be retrieved from the [Retrieve Unspent Inputs endpoint.](https://developers.fireblocks.com/reference/get_vault-accounts-vaultaccountid-assetid-unspent-inputs)  For &#x60;RAW&#x60; operations, add the key &#x60;rawMessageData&#x60; with the value set to the [raw message data structure.](https://developers.fireblocks.com/reference/raw-signing-objects#rawmessagedata)  For &#x60;CONTRACT_CALL&#x60; operations, add the key &#x60;contractCallData&#x60; with the value set to the Ethereum smart contract Application Binary Interface (ABI) payload. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions.  | [optional] 
**customer_ref_id** | **str** | The ID for AML providers to associate the owner of funds with transactions. | [optional] 
**travel_rule_message** | [**TravelRuleCreateTransactionRequest**](TravelRuleCreateTransactionRequest.md) |  | [optional] 
**auto_staking** | **bool** | This feature is no longer supported. | [optional] 
**network_staking** | [**TransactionRequestNetworkStaking**](TransactionRequestNetworkStaking.md) |  | [optional] 
**cpu_staking** | [**TransactionRequestNetworkStaking**](TransactionRequestNetworkStaking.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.transaction_request import TransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequest from a JSON string
transaction_request_instance = TransactionRequest.from_json(json)
# print the JSON string representation of the object
print TransactionRequest.to_json()

# convert the object into a dict
transaction_request_dict = transaction_request_instance.to_dict()
# create an instance of TransactionRequest from a dict
transaction_request_form_dict = transaction_request.from_dict(transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


