# TradeClass

The class of trade a pair represents, derived from the asset class of each leg, the chains those assets settle on, where the trade executes, and the trading side: * **SWAP_DEFI** - Exchange between two crypto assets on the same chain, executed on-chain * **SWAP_CEFI** - Exchange between two crypto assets on the same chain, executed through a provider account * **BRIDGE_DEFI** - Exchange between two crypto assets on different chains, executed on-chain * **BRIDGE_CEFI** - Exchange between two crypto assets on different chains, executed through a provider account * **INTERNAL_LEDGER** - Exchange between two crypto assets settled on a provider's internal ledger, within a single provider account. Not split by chain, because neither leg settles on-chain while the trade executes * **ON_RAMP** - Buying a crypto asset with a fiat asset * **OFF_RAMP** - Selling a crypto asset for a fiat asset * **FX** - Exchange between two fiat assets * **OTC** - A pair quoted by an OTC desk: firm, short-lived RFQ commitments against a dealer, executed on credit rather than against an order book. Takes precedence over the asset-class values, so an OTC desk selling USDC for USD is `OTC`, not `OFF_RAMP` * **UNKNOWN** - The class could not be resolved, e.g. when the chain of an asset could not be determined. Callers should not route on a pair with this class 

## Enum

* `SWAP_DEFI` (value: `'SWAP_DEFI'`)

* `SWAP_CEFI` (value: `'SWAP_CEFI'`)

* `BRIDGE_DEFI` (value: `'BRIDGE_DEFI'`)

* `BRIDGE_CEFI` (value: `'BRIDGE_CEFI'`)

* `INTERNAL_LEDGER` (value: `'INTERNAL_LEDGER'`)

* `ON_RAMP` (value: `'ON_RAMP'`)

* `OFF_RAMP` (value: `'OFF_RAMP'`)

* `FX` (value: `'FX'`)

* `OTC` (value: `'OTC'`)

* `UNKNOWN` (value: `'UNKNOWN'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


