# ExecutionDisbursementOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**status** | [**ExecutionOperationStatus**](ExecutionOperationStatus.md) |  | 
**validation_failure** | [**DisbursementValidationFailure**](DisbursementValidationFailure.md) |  | [optional] 
**operation_type** | [**DisbursementOperationType**](DisbursementOperationType.md) |  | 
**preview** | [**DisbursementOperationPreview**](DisbursementOperationPreview.md) |  | [optional] 
**execution** | [**DisbursementOperationExecution**](DisbursementOperationExecution.md) |  | [optional] 

## Example

```python
from fireblocks.models.execution_disbursement_operation import ExecutionDisbursementOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionDisbursementOperation from a JSON string
execution_disbursement_operation_instance = ExecutionDisbursementOperation.from_json(json)
# print the JSON string representation of the object
print(ExecutionDisbursementOperation.to_json())

# convert the object into a dict
execution_disbursement_operation_dict = execution_disbursement_operation_instance.to_dict()
# create an instance of ExecutionDisbursementOperation from a dict
execution_disbursement_operation_from_dict = ExecutionDisbursementOperation.from_dict(execution_disbursement_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


