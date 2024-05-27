# WorkflowExecutionOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**status** | [**ExecutionOperationStatus**](ExecutionOperationStatus.md) |  | 
**operation_type** | [**DisbursementOperationType**](DisbursementOperationType.md) |  | 
**validation_failure** | [**DisbursementValidationFailure**](DisbursementValidationFailure.md) |  | [optional] 
**execution** | [**DisbursementOperationExecution**](DisbursementOperationExecution.md) |  | [optional] 
**preview** | [**DisbursementOperationPreview**](DisbursementOperationPreview.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.workflow_execution_operation import WorkflowExecutionOperation

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecutionOperation from a JSON string
workflow_execution_operation_instance = WorkflowExecutionOperation.from_json(json)
# print the JSON string representation of the object
print WorkflowExecutionOperation.to_json()

# convert the object into a dict
workflow_execution_operation_dict = workflow_execution_operation_instance.to_dict()
# create an instance of WorkflowExecutionOperation from a dict
workflow_execution_operation_form_dict = workflow_execution_operation.from_dict(workflow_execution_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


