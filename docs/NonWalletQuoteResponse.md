# NonWalletQuoteResponse

Return a quote that cannot be used for a swap operation.

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
**estimated_fees** | [**NonWalletQuoteFee**](NonWalletQuoteFee.md) |  | 

## Example

```python
from fireblocks.models.non_wallet_quote_response import NonWalletQuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NonWalletQuoteResponse from a JSON string
non_wallet_quote_response_instance = NonWalletQuoteResponse.from_json(json)
# print the JSON string representation of the object
print(NonWalletQuoteResponse.to_json())

# convert the object into a dict
non_wallet_quote_response_dict = non_wallet_quote_response_instance.to_dict()
# create an instance of NonWalletQuoteResponse from a dict
non_wallet_quote_response_from_dict = NonWalletQuoteResponse.from_dict(non_wallet_quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


