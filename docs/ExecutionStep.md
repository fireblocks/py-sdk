# ExecutionStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExecutionStepType**](ExecutionStepType.md) |  | 
**status** | [**ExecutionStepStatusEnum**](ExecutionStepStatusEnum.md) |  | 
**fee** | [**Fee**](Fee.md) |  | [optional] 
**tx_id** | **str** |  | [optional] 
**tx_hash** | **str** |  | [optional] 
**error** | [**ExecutionStepError**](ExecutionStepError.md) |  | [optional] 

## Example

```python
from fireblocks.models.execution_step import ExecutionStep

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionStep from a JSON string
execution_step_instance = ExecutionStep.from_json(json)
# print the JSON string representation of the object
print(ExecutionStep.to_json())

# convert the object into a dict
execution_step_dict = execution_step_instance.to_dict()
# create an instance of ExecutionStep from a dict
execution_step_from_dict = ExecutionStep.from_dict(execution_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


