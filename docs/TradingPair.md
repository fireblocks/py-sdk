# TradingPair

A supported base/quote asset pair for a provider, optionally scoped to a specific connected account, for a given trading side (BUY/SELL, or `BOTH`), with the transfer rails and amount limits that apply to it. `baseAssetId` / `quoteAssetId` may be the wildcard `*`, meaning any asset on `baseChain` / `quoteChain`; such a row is not expanded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider that supports this pair. | 
**account_id** | **str** | The connected account the pair is scoped to. Absent for direct-access providers, and for provider-level pairs that describe what a provider supports before any account is connected. Its absence therefore does not imply the provider is direct-access. | [optional] 
**base_asset_id** | **str** | Fireblocks asset ID of the base asset, or &#x60;*&#x60; for any asset on &#x60;baseChain&#x60;. A &#x60;*&#x60; value always comes with &#x60;baseChain&#x60; set. | 
**quote_asset_id** | **str** | Fireblocks asset ID of the quote asset, or &#x60;*&#x60; for any asset on &#x60;quoteChain&#x60;. A &#x60;*&#x60; value always comes with &#x60;quoteChain&#x60; set. | 
**base_chain** | **str** | Blockchain &#x60;legacyId&#x60; of the base asset (e.g. &#x60;ETH&#x60;, &#x60;BASECHAIN_ETH&#x60;, &#x60;ETH-AETH&#x60;, &#x60;SOL&#x60;). Set for leaf crypto assets; absent for fiat and virtual assets. | [optional] 
**quote_chain** | **str** | Blockchain &#x60;legacyId&#x60; of the quote asset (e.g. &#x60;ETH&#x60;, &#x60;BASECHAIN_ETH&#x60;, &#x60;ETH-AETH&#x60;, &#x60;SOL&#x60;). Set for leaf crypto assets; absent for fiat and virtual assets. | [optional] 
**side** | [**TradingPairSide**](TradingPairSide.md) |  | 
**trade_class** | [**TradeClass**](TradeClass.md) |  | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**prefunded** | **bool** | Whether the provider requires the funds to be prefunded on the provider account before the order can execute. | [optional] 
**min** | **str** | Minimum amount of the base asset for this pair/side, as a decimal string. | [optional] 
**max** | **str** | Maximum amount of the base asset for this pair/side, as a decimal string. | [optional] 

## Example

```python
from fireblocks.models.trading_pair import TradingPair

# TODO update the JSON string below
json = "{}"
# create an instance of TradingPair from a JSON string
trading_pair_instance = TradingPair.from_json(json)
# print the JSON string representation of the object
print(TradingPair.to_json())

# convert the object into a dict
trading_pair_dict = trading_pair_instance.to_dict()
# create an instance of TradingPair from a dict
trading_pair_from_dict = TradingPair.from_dict(trading_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


