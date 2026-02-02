# OrderExecutionStep


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
from fireblocks.models.order_execution_step import OrderExecutionStep

# TODO update the JSON string below
json = "{}"
# create an instance of OrderExecutionStep from a JSON string
order_execution_step_instance = OrderExecutionStep.from_json(json)
# print the JSON string representation of the object
print(OrderExecutionStep.to_json())

# convert the object into a dict
order_execution_step_dict = order_execution_step_instance.to_dict()
# create an instance of OrderExecutionStep from a dict
order_execution_step_from_dict = OrderExecutionStep.from_dict(order_execution_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


