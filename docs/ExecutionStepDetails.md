# ExecutionStepDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExecutionStepType**](ExecutionStepType.md) |  | 
**fee** | [**Fee**](Fee.md) |  | [optional] 

## Example

```python
from fireblocks.models.execution_step_details import ExecutionStepDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionStepDetails from a JSON string
execution_step_details_instance = ExecutionStepDetails.from_json(json)
# print the JSON string representation of the object
print(ExecutionStepDetails.to_json())

# convert the object into a dict
execution_step_details_dict = execution_step_details_instance.to_dict()
# create an instance of ExecutionStepDetails from a dict
execution_step_details_from_dict = ExecutionStepDetails.from_dict(execution_step_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


