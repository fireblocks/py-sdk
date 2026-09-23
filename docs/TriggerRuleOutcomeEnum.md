# TriggerRuleOutcomeEnum

Whether the step's trigger rules caused its connector to run. This is a decision about running, not about risk — `ACCEPT`/`REJECT` belong to the outcome fields.  - `EXECUTE` — a rule called for screening, so the connector ran - `PASS` — a rule let the subject through without screening - `FAIL` — the step could not run; see `bypassReason` 

## Enum

* `EXECUTE` (value: `'EXECUTE'`)

* `PASS` (value: `'PASS'`)

* `FAIL` (value: `'FAIL'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


