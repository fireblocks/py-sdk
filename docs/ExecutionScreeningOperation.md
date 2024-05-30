# ExecutionScreeningOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**status** | [**ExecutionOperationStatus**](ExecutionOperationStatus.md) |  | 
**operation_type** | [**ScreeningOperationType**](ScreeningOperationType.md) |  | 
**validation_failure** | [**ScreeningValidationFailure**](ScreeningValidationFailure.md) |  | [optional] 
**execution** | [**ScreeningOperationExecution**](ScreeningOperationExecution.md) |  | [optional] 

## Example

```python
from fireblocks.models.execution_screening_operation import ExecutionScreeningOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionScreeningOperation from a JSON string
execution_screening_operation_instance = ExecutionScreeningOperation.from_json(json)
# print the JSON string representation of the object
print(ExecutionScreeningOperation.to_json())

# convert the object into a dict
execution_screening_operation_dict = execution_screening_operation_instance.to_dict()
# create an instance of ExecutionScreeningOperation from a dict
execution_screening_operation_from_dict = ExecutionScreeningOperation.from_dict(execution_screening_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


