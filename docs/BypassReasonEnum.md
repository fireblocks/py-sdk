# BypassReasonEnum

Why a step's screening did not run. A verbatim mirror of the platform's `BypassReason` vocabulary, shared with the rest of Fireblocks screening.  Only `PASSED_BY_POLICY` is an approval — the policy deliberately let the subject through. Every other value means the check could not be performed, and the step is rejected rather than passed. A bypass is not a pass.  - `MANUAL` — a person bypassed it - `UNSUPPORTED_ASSET` — the provider does not screen this asset or chain - `UNSUPPORTED_ROUTE` — the provider does not screen this route - `PASSED_BY_POLICY` — a policy rule let it through without screening - `BYPASSED_FAILURE` — screening failed and policy allowed a bypass - `TIMED_OUT` — the provider did not answer within the deadline - `BAD_CREDENTIALS` — the tenant's provider credentials were rejected - `CONFIGURATION_ERROR` — the connector is misconfigured for this tenant - `DROPPED_BY_BLOCKCHAIN` — the transaction never confirmed - `PROCESS_DISMISSED` — the surrounding process was cancelled 

## Enum

* `MANUAL` (value: `'MANUAL'`)

* `UNSUPPORTED_ASSET` (value: `'UNSUPPORTED_ASSET'`)

* `UNSUPPORTED_ROUTE` (value: `'UNSUPPORTED_ROUTE'`)

* `PASSED_BY_POLICY` (value: `'PASSED_BY_POLICY'`)

* `BYPASSED_FAILURE` (value: `'BYPASSED_FAILURE'`)

* `TIMED_OUT` (value: `'TIMED_OUT'`)

* `BAD_CREDENTIALS` (value: `'BAD_CREDENTIALS'`)

* `CONFIGURATION_ERROR` (value: `'CONFIGURATION_ERROR'`)

* `DROPPED_BY_BLOCKCHAIN` (value: `'DROPPED_BY_BLOCKCHAIN'`)

* `PROCESS_DISMISSED` (value: `'PROCESS_DISMISSED'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


