# ConversionOperationExecution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**ConversionOperationConfigParams**](ConversionOperationConfigParams.md) |  | 
**output** | [**ConversionOperationExecutionOutput**](ConversionOperationExecutionOutput.md) |  | [optional] 
**started_at** | **float** |  | 
**finished_at** | **float** |  | [optional] 
**failure** | [**ConversionOperationFailure**](ConversionOperationFailure.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.conversion_operation_execution import ConversionOperationExecution

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionOperationExecution from a JSON string
conversion_operation_execution_instance = ConversionOperationExecution.from_json(json)
# print the JSON string representation of the object
print ConversionOperationExecution.to_json()

# convert the object into a dict
conversion_operation_execution_dict = conversion_operation_execution_instance.to_dict()
# create an instance of ConversionOperationExecution from a dict
conversion_operation_execution_form_dict = conversion_operation_execution.from_dict(conversion_operation_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


