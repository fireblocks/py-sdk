# ScreeningOperationEnum

What the caller wants Compliance Orchestrator to do. The target workflow must have a step configured for the operation; the error names the supported set when it does not.  - `ADDRESS_SCREENING` — screen an address on its own, before anything exists   on-chain. Answers whether the address itself carries risk. - `TRANSACTION_SCREENING` — screen a whole transfer: source and destination,   amount and direction, not the destination alone. - `REGISTER_TRANSACTION` — record a confirmed transfer with the provider for   ongoing monitoring. Not a gate: it files the transfer so the provider's own   rules can raise alerts later, which is what feeds its AML model. 

## Enum

* `ADDRESS_SCREENING` (value: `'ADDRESS_SCREENING'`)

* `TRANSACTION_SCREENING` (value: `'TRANSACTION_SCREENING'`)

* `REGISTER_TRANSACTION` (value: `'REGISTER_TRANSACTION'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


