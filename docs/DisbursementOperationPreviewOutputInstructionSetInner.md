# DisbursementOperationPreviewOutputInstructionSetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**AssetAmount**](AssetAmount.md) |  | 
**fee** | [**AssetAmount**](AssetAmount.md) |  | 
**payee_account** | [**Destination**](Destination.md) |  | 
**time_seconds** | **float** |  | 

## Example

```python
from fireblocks.models.disbursement_operation_preview_output_instruction_set_inner import DisbursementOperationPreviewOutputInstructionSetInner

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementOperationPreviewOutputInstructionSetInner from a JSON string
disbursement_operation_preview_output_instruction_set_inner_instance = DisbursementOperationPreviewOutputInstructionSetInner.from_json(json)
# print the JSON string representation of the object
print(DisbursementOperationPreviewOutputInstructionSetInner.to_json())

# convert the object into a dict
disbursement_operation_preview_output_instruction_set_inner_dict = disbursement_operation_preview_output_instruction_set_inner_instance.to_dict()
# create an instance of DisbursementOperationPreviewOutputInstructionSetInner from a dict
disbursement_operation_preview_output_instruction_set_inner_from_dict = DisbursementOperationPreviewOutputInstructionSetInner.from_dict(disbursement_operation_preview_output_instruction_set_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


