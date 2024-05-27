# ScreeningOperationExecution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | [**ScreeningOperationExecutionOutput**](ScreeningOperationExecutionOutput.md) |  | [optional] 
**started_at** | **float** |  | 
**finished_at** | **float** |  | [optional] 
**failure** | [**ScreeningOperationFailure**](ScreeningOperationFailure.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.screening_operation_execution import ScreeningOperationExecution

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningOperationExecution from a JSON string
screening_operation_execution_instance = ScreeningOperationExecution.from_json(json)
# print the JSON string representation of the object
print ScreeningOperationExecution.to_json()

# convert the object into a dict
screening_operation_execution_dict = screening_operation_execution_instance.to_dict()
# create an instance of ScreeningOperationExecution from a dict
screening_operation_execution_form_dict = screening_operation_execution.from_dict(screening_operation_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


