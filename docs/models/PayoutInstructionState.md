# fireblocks_client.model.payout_instruction_state.PayoutInstructionState

- NOT_STARTED - waiting to start - TRANSACTION_SENT - an underlying transaction was sent - COMPLETED - completed successfully - FAILED - failed - TRANSLATION_ERROR -lookup of the destination failed (due to changes in the underlying whitelisted external wallet or similar) - SKIPPED- no transaction(s) created for this instruction 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | - NOT_STARTED - waiting to start - TRANSACTION_SENT - an underlying transaction was sent - COMPLETED - completed successfully - FAILED - failed - TRANSLATION_ERROR -lookup of the destination failed (due to changes in the underlying whitelisted external wallet or similar) - SKIPPED- no transaction(s) created for this instruction  | must be one of ["NOT_STARTED", "TRANSACTION_SENT", "COMPLETED", "FAILED", "TRANSLATION_ERROR", "SKIPPED", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

