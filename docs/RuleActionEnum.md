# RuleActionEnum

What happens when a rule matches. Which values are legal depends on the rule set the rule belongs to — a trigger rule decides whether to screen, an outcome rule decides what the answer means. The enum is the union of both sets, so neither set accepts all of its values: `FREEZE` is the one value shared by the two, and every other value belongs to exactly one of them.  Trigger rules:  - `SCREEN` — call the connector - `PASS` — let the subject through without screening - `FREEZE` — hold for manual action  Outcome rules:  - `ACCEPT` — the step passes - `REJECT` — the step fails - `ALERT` — the step passes but is flagged for review - `FREEZE` — hold for manual action - `WAIT` — come back later; refused once the deadline has passed 

## Enum

* `SCREEN` (value: `'SCREEN'`)

* `PASS` (value: `'PASS'`)

* `FREEZE` (value: `'FREEZE'`)

* `ACCEPT` (value: `'ACCEPT'`)

* `REJECT` (value: `'REJECT'`)

* `ALERT` (value: `'ALERT'`)

* `WAIT` (value: `'WAIT'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


