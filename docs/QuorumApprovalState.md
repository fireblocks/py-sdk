# QuorumApprovalState

Whether an approval requirement has been met. Treat this as authoritative rather than comparing the counts yourself: a group can show `currentApprovalCount` equal to `threshold` and still be `PENDING` when the request additionally requires the workspace owner's approval.

## Enum

* `APPROVED` (value: `'APPROVED'`)

* `PENDING` (value: `'PENDING'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


