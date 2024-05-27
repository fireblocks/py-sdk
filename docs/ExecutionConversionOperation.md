# ExecutionConversionOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**status** | [**ExecutionOperationStatus**](ExecutionOperationStatus.md) |  | 
**validation_failure** | [**ConversionValidationFailure**](ConversionValidationFailure.md) |  | [optional] 
**operation_type** | [**ConversionOperationType**](ConversionOperationType.md) |  | 
**preview** | [**ConversionOperationPreview**](ConversionOperationPreview.md) |  | [optional] 
**execution** | [**ConversionOperationExecution**](ConversionOperationExecution.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.execution_conversion_operation import ExecutionConversionOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionConversionOperation from a JSON string
execution_conversion_operation_instance = ExecutionConversionOperation.from_json(json)
# print the JSON string representation of the object
print ExecutionConversionOperation.to_json()

# convert the object into a dict
execution_conversion_operation_dict = execution_conversion_operation_instance.to_dict()
# create an instance of ExecutionConversionOperation from a dict
execution_conversion_operation_form_dict = execution_conversion_operation.from_dict(execution_conversion_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


