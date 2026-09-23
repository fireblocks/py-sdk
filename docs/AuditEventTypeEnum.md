# AuditEventTypeEnum

The kind of event an audit entry records.  - `STATUS_TRANSITION` — the screening moved between statuses - `STEP_TRIGGER_RULE_EVALUATED` — a step's trigger rules were evaluated - `CONNECTOR_CALL` — a connector was called; `data.phase` distinguishes the   request from its terminal result - `STEP_OUTCOME_RULE_EVALUATED` — a step's outcome rules read the response - `STEP_METADATA_RECORDED` — connector metadata was attached to a step - `WORKFLOW_OUTCOME` — the workflow outcome was derived from its steps. 

## Enum

* `STATUS_TRANSITION` (value: `'STATUS_TRANSITION'`)

* `STEP_TRIGGER_RULE_EVALUATED` (value: `'STEP_TRIGGER_RULE_EVALUATED'`)

* `CONNECTOR_CALL` (value: `'CONNECTOR_CALL'`)

* `STEP_OUTCOME_RULE_EVALUATED` (value: `'STEP_OUTCOME_RULE_EVALUATED'`)

* `STEP_METADATA_RECORDED` (value: `'STEP_METADATA_RECORDED'`)

* `WORKFLOW_OUTCOME` (value: `'WORKFLOW_OUTCOME'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


