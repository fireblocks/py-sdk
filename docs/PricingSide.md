# PricingSide

Side to price on a quote, rate or offer request. BUY: receive base / pay quote; SELL: give base / receive quote; BOTH: request pricing for both sides at once. Providers that support only one of the sides return entries for that side only. BOTH is accepted on requests only, never on order execution requests, and responses never return it: every returned quote, rate or offer carries a concrete BUY or SELL. When omitted, defaults to SELL.

## Enum

* `BUY` (value: `'BUY'`)

* `SELL` (value: `'SELL'`)

* `BOTH` (value: `'BOTH'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


