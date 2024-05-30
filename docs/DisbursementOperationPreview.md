# DisbursementOperationPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**DisbursementOperationInput**](DisbursementOperationInput.md) |  | 
**output** | [**DisbursementOperationPreviewOutput**](DisbursementOperationPreviewOutput.md) |  | [optional] 
**failure** | [**OperationExecutionFailure**](OperationExecutionFailure.md) |  | [optional] 

## Example

```python
from fireblocks.models.disbursement_operation_preview import DisbursementOperationPreview

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementOperationPreview from a JSON string
disbursement_operation_preview_instance = DisbursementOperationPreview.from_json(json)
# print the JSON string representation of the object
print(DisbursementOperationPreview.to_json())

# convert the object into a dict
disbursement_operation_preview_dict = disbursement_operation_preview_instance.to_dict()
# create an instance of DisbursementOperationPreview from a dict
disbursement_operation_preview_from_dict = DisbursementOperationPreview.from_dict(disbursement_operation_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


