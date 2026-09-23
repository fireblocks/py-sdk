# WorkflowStatusEnum

A workflow's status, which controls whether it can be screened against.  - `DRAFT` — the editing state. Rules can be changed while nothing is   screening against them, so a screening never runs against a half-finished   configuration. - `ACTIVE` — `POST /v1/compliance/orchestrator/screenings` accepts screenings against this workflow. 

## Enum

* `ACTIVE` (value: `'ACTIVE'`)

* `DRAFT` (value: `'DRAFT'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


