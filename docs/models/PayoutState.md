# fireblocks_client.model.payout_state.PayoutState

- CREATED - payout instruction set created with all its details - FILE_FOUND - new file found in the FTP - REQUESTED - payout requested with all its details - TRANSLATED - payout instruction account IDs identified and translated - PROCESSING - payout instruction set executed and is processing - SUBMITTED - transactions submitted for payout instructions - FINALIZED - payout finished processing, all transactions processed successfully - INSUFFICIENT_BALANCE - insufficient balance in the payment account (can be a temporary state) - FAILED - one or more of the payout instructions failed 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | - CREATED - payout instruction set created with all its details - FILE_FOUND - new file found in the FTP - REQUESTED - payout requested with all its details - TRANSLATED - payout instruction account IDs identified and translated - PROCESSING - payout instruction set executed and is processing - SUBMITTED - transactions submitted for payout instructions - FINALIZED - payout finished processing, all transactions processed successfully - INSUFFICIENT_BALANCE - insufficient balance in the payment account (can be a temporary state) - FAILED - one or more of the payout instructions failed  | must be one of ["CREATED", "FILE_FOUND", "REQUESTED", "TRANSLATED", "PROCESSING", "SUBMITTED", "FINALIZED", "INSUFFICIENT_BALANCE", "FAILED", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

