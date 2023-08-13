# fireblocks_client.model.payout_status.PayoutStatus

- REQUESTED payout requested with all its details - VERIFIED payout instruction set details were verified - PROCESSING payout instruction set executed and is processing - FINALIZED payout done (all payout instructions completed successfully) - INSUFFICIENT_BALANCE insufficient balance in the payment account (can be a temporary state) - FAILED one or more of the payout instructions failed 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | - REQUESTED payout requested with all its details - VERIFIED payout instruction set details were verified - PROCESSING payout instruction set executed and is processing - FINALIZED payout done (all payout instructions completed successfully) - INSUFFICIENT_BALANCE insufficient balance in the payment account (can be a temporary state) - FAILED one or more of the payout instructions failed  | must be one of ["REGISTERED", "VERIFYING", "IN_PROGRESS", "DONE", "INSUFFICIENT_BALANCE", "FAILED", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

