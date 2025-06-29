# WalletQuoteResponse

Return a quote with id that can be used for swap operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | [**SwapProviderProtocolsEnum**](SwapProviderProtocolsEnum.md) |  | 
**input_amount** | **str** | The amount of tokens the swapper will provide | 
**input_asset** | **str** | The id of the asset the swapper will provide | 
**slippage_tolerance** | **float** | The slippage tolerance is a percentage. The slippage tolerance is the maximum amount the price can change between the time the transaction is submitted and the time it is executed | 
**output_min_amount** | **str** | The minimum amount of tokens the swapper will receive | 
**output_max_amount** | **str** | Maximum amount of tokens that the swapper will receive | 
**output_asset** | **str** | The id of the asset the swapper will receive | 
**additional_data** | [**ProviderAdditionalData**](ProviderAdditionalData.md) |  | 
**provider_quote_id** | **str** | An identifier that uniquely identifies the received quote | 
**expired_at** | **datetime** | When was the received &#x60;providerQuoteId&#x60; is expired (ISO Date time). | 
**required_actions** | [**List[SwapRequiredActionsEnum]**](SwapRequiredActionsEnum.md) | The required actions for completing a swap operation | 
**estimated_fees** | [**QuoteFee**](QuoteFee.md) |  | 

## Example

```python
from fireblocks.models.wallet_quote_response import WalletQuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WalletQuoteResponse from a JSON string
wallet_quote_response_instance = WalletQuoteResponse.from_json(json)
# print the JSON string representation of the object
print(WalletQuoteResponse.to_json())

# convert the object into a dict
wallet_quote_response_dict = wallet_quote_response_instance.to_dict()
# create an instance of WalletQuoteResponse from a dict
wallet_quote_response_from_dict = WalletQuoteResponse.from_dict(wallet_quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


