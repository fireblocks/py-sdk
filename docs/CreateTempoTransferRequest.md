# CreateTempoTransferRequest

Request body for creating a Tempo transfer transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | A custom note that can be associated with the transaction. | [optional] 
**external_tx_id** | **str** | Unique ID provided by the customer, used to identify the transaction. | [optional] 
**fee_currency** | **str** | The asset ID used to pay the transaction fee, if different from assetId. Maps to FeeParams.feeCurrency. Must be a valid fee token for &#x60;assetId&#x60; (e.g. a TIP-20 gas token for the base asset); an invalid pairing surfaces as 400 INVALID_FEE_CURRENCY_PARAM. | [optional] 
**asset_id** | **str** | The ID of the asset to transfer. Must be a non-deprecated asset supported on a Tempo-eligible blockchain; an unknown, deprecated, or unsupported asset surfaces as 400 UNSUPPORTED_ASSET. | 
**source** | [**TempoTransferSource**](TempoTransferSource.md) |  | 
**destination** | [**TempoTransferDestination**](TempoTransferDestination.md) |  | [optional] 
**amount** | **str** | The amount to transfer, as a numeric string. Required when &#x60;destination&#x60; is set; must be omitted when &#x60;destinations&#x60; is set (each entry carries its own amount instead). | [optional] 
**treat_as_gross_amount** | **bool** | If true, the specified amount includes the fee (fee is deducted from amount). | [optional] 
**fee_level** | **str** | The fee level to use, mutually exclusive with an explicit custom fee. | [optional] 
**travel_rule_message** | **str** | Beta. An opaque travel-rule payload. | [optional] 
**travel_rule_message_id** | **str** | Beta. An identifier of a TravelRule message, already sent to the TravelRule provider. | [optional] 
**use_gasless** | **bool** | Opt in to fee-payer-sponsored (gasless) transfer. | [optional] 
**configurations** | [**TransactionConfigurations**](TransactionConfigurations.md) |  | [optional] 
**max_fee_per_gas** | **str** | The maximum total fee per gas the sender is willing to pay, in wei. | [optional] 
**max_priority_fee_per_gas** | **str** | The maximum priority fee (tip) per gas the sender is willing to pay, in wei. | [optional] 
**destinations** | [**List[TempoTransferDestinationItem]**](TempoTransferDestinationItem.md) | Multiple destinations for a single transfer. Mutually exclusive with &#x60;destination&#x60;. | [optional] 
**fail_on_low_fee** | **bool** | Beta. If true, fail the transaction rather than sending it with a low fee. | [optional] 
**gas_limit** | **str** | The gas limit for the transaction. | [optional] 
**replace_tx_by_hash** | **str** | Beta. The hash of the EVM transaction to replace (RBF). | [optional] 
**fee_payer_account_id** | **str** | Vault account ID of the fee payer sponsoring this transfer. | [optional] 
**nonce_strategy** | **str** | Tempo&#39;s 2-dimensional nonce strategy: &#x60;SEQUENTIAL&#x60; runs under a single nonce lane (lane 0); &#x60;USER_DEFINED_LANE&#x60; runs in parallel under a specified lane (1–16), and requires &#x60;nonceLane&#x60;; &#x60;EXPIRING&#x60; marks the transaction with an expiry of up to 5 minutes (Tempo-defined) and does not use &#x60;nonceLane&#x60;. | [optional] 
**nonce_lane** | **int** | The nonce lane to use, 1–16. Required and only meaningful when nonceStrategy is USER_DEFINED_LANE; not used for SEQUENTIAL or EXPIRING. | [optional] 
**memo** | **str** | Beta. Tempo TIP-20 memo (max 32 bytes). | [optional] 

## Example

```python
from fireblocks.models.create_tempo_transfer_request import CreateTempoTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTempoTransferRequest from a JSON string
create_tempo_transfer_request_instance = CreateTempoTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTempoTransferRequest.to_json())

# convert the object into a dict
create_tempo_transfer_request_dict = create_tempo_transfer_request_instance.to_dict()
# create an instance of CreateTempoTransferRequest from a dict
create_tempo_transfer_request_from_dict = CreateTempoTransferRequest.from_dict(create_tempo_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


