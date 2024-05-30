# ScreeningOperationExecutionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verdicts** | [**List[ScreeningVerdict]**](ScreeningVerdict.md) |  | 

## Example

```python
from fireblocks_client.models.screening_operation_execution_output import ScreeningOperationExecutionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningOperationExecutionOutput from a JSON string
screening_operation_execution_output_instance = ScreeningOperationExecutionOutput.from_json(json)
# print the JSON string representation of the object
print(ScreeningOperationExecutionOutput.to_json())

# convert the object into a dict
screening_operation_execution_output_dict = screening_operation_execution_output_instance.to_dict()
# create an instance of ScreeningOperationExecutionOutput from a dict
screening_operation_execution_output_from_dict = ScreeningOperationExecutionOutput.from_dict(screening_operation_execution_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


