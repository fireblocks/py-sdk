# TransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**TransactionOperation**](TransactionOperation.md) |  | [optional] [default to TransactionOperation.TRANSFER]
**note** | **str** | Custom note, not sent to the blockchain, to describe the transaction at your Fireblocks workspace. | [optional] 
**external_tx_id** | **str** | This parameter allows you to add a unique ID of your own to help prevent duplicate transactions. No specific format is required for this parameter. After you submit a transaction with an external ID, Fireblocks will automatically reject all future transactions with the same ID. Using an external ID primarily helps in situations where, even though a submitted transaction responds with an error due to an internet outage,  the transaction was still sent to and processed on the blockchain.  Use the [Get a specific transaction by external transaction ID](https://developers.fireblocks.com/reference/gettransactionbyexternalid)  endpoint to validate whether these transactions have been processed. | [optional] 
**asset_id** | **str** | The ID of the asset to transfer, for &#x60;TRANSFER&#x60;, &#x60;MINT&#x60; or &#x60;BURN&#x60; operations. [See the list of supported assets and their IDs on Fireblocks.](https://developers.fireblocks.com/reference/gettrlinksupportedasset#/) | [optional] 
**source** | [**SourceTransferPeerPath**](SourceTransferPeerPath.md) |  | [optional] 
**destination** | [**DestinationTransferPeerPath**](DestinationTransferPeerPath.md) |  | [optional] 
**destinations** | [**List[TransactionRequestDestination]**](TransactionRequestDestination.md) | For UTXO based blockchains, you can send a single transaction to multiple destinations. | [optional] 
**amount** | [**TransactionRequestAmount**](TransactionRequestAmount.md) |  | [optional] 
**treat_as_gross_amount** | **bool** | \&quot;When set to &#x60;true&#x60;, the fee will be deducted from the requested amount.\&quot;  **Note**: This parameter can only be considered if a transaction’s asset is a base asset, such as ETH or MATIC. If the asset can’t be used for transaction fees, like USDC, this parameter is ignored and the fee is deducted from the relevant base asset wallet in the source account. | [optional] 
**force_sweep** | **bool** | For Polkadot, Kusama and Westend transactions only. When set to true, Fireblocks will empty the asset wallet.     **Note:** If set to true when the source account is exactly 1 DOT, the transaction will fail. Any amount more or less than 1 DOT succeeds. This is a Polkadot blockchain limitation. | [optional] 
**fee_level** | **str** | For UTXO, EVM-based, or Solana blockchains only. Defines the blockchain fee level which will be payed for the transaction. Alternatively, specific fee estimation parameters exist below. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 
**priority_fee** | [**TransactionRequestPriorityFee**](TransactionRequestPriorityFee.md) |  | [optional] 
**fail_on_low_fee** | **bool** | When set to &#x60;true&#x60;, in case the current &#x60;MEDIUM&#x60; fee level is higher than the one specified in the transaction, the transaction will fail to avoid getting stuck with no confirmations. | [optional] 
**max_fee** | **str** | The maximum fee (gas price or fee per byte) that should be payed for the transaction.  In case the current value of the requested &#x60;feeLevel&#x60; is higher than this requested maximum fee.  Represented by a numeric string for accurate precision. | [optional] 
**max_total_fee** | **str** | For BTC-based blockchains only. The maximum fee (in the units of the fee-paying asset) that should be paid for the transaction. | [optional] 
**gas_limit** | [**TransactionRequestGasLimit**](TransactionRequestGasLimit.md) |  | [optional] 
**gas_price** | [**TransactionRequestGasPrice**](TransactionRequestGasPrice.md) |  | [optional] 
**network_fee** | [**TransactionRequestNetworkFee**](TransactionRequestNetworkFee.md) |  | [optional] 
**replace_tx_by_hash** | **str** | For EVM-based blockchains only. In case a transaction is stuck, specify the hash of the stuck transaction to replace it by this transaction with a higher fee, or to replace it with this transaction with a zero fee and drop it from the blockchain. | [optional] 
**extra_parameters** | [**ExtraParameters**](ExtraParameters.md) |  | [optional] 
**customer_ref_id** | **str** | The ID for AML providers to associate the owner of funds with transactions. | [optional] 
**travel_rule_message** | [**TravelRuleCreateTransactionRequest**](TravelRuleCreateTransactionRequest.md) |  | [optional] 
**travel_rule_message_id** | **str** | The ID of the travel rule message from any travel rule provider. Used for travel rule supporting functionality to associate transactions with existing travel rule messages. | [optional] 
**auto_staking** | **bool** | This feature is no longer supported. | [optional] 
**network_staking** | [**TransactionRequestNetworkStaking**](TransactionRequestNetworkStaking.md) |  | [optional] 
**cpu_staking** | [**TransactionRequestNetworkStaking**](TransactionRequestNetworkStaking.md) |  | [optional] 
**use_gasless** | **bool** | - Override the default gasless configuration by sending true\\false | [optional] 

## Example

```python
from fireblocks.models.transaction_request import TransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequest from a JSON string
transaction_request_instance = TransactionRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionRequest.to_json())

# convert the object into a dict
transaction_request_dict = transaction_request_instance.to_dict()
# create an instance of TransactionRequest from a dict
transaction_request_from_dict = TransactionRequest.from_dict(transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


