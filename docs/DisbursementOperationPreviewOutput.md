# DisbursementOperationPreviewOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruction_set** | [**List[DisbursementOperationPreviewOutputInstructionSetInner]**](DisbursementOperationPreviewOutputInstructionSetInner.md) |  | 

## Example

```python
from fireblocks_client.models.disbursement_operation_preview_output import DisbursementOperationPreviewOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementOperationPreviewOutput from a JSON string
disbursement_operation_preview_output_instance = DisbursementOperationPreviewOutput.from_json(json)
# print the JSON string representation of the object
print(DisbursementOperationPreviewOutput.to_json())

# convert the object into a dict
disbursement_operation_preview_output_dict = disbursement_operation_preview_output_instance.to_dict()
# create an instance of DisbursementOperationPreviewOutput from a dict
disbursement_operation_preview_output_from_dict = DisbursementOperationPreviewOutput.from_dict(disbursement_operation_preview_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


