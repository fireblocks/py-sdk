# StepConfig

One step in a workflow, backed by a single connector.  A connector is the compliance provider integration that does the work — `kyt_trmlabs` is TRM Labs. The step declares which operations that connector handles; a screening naming an operation no step is configured for is refused, and the error reports the supported set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **str** | Unique within the workflow. | 
**connector_id** | **str** | Identifies which connector this step invokes. | 
**operations** | [**List[StepOperationConfig]**](StepOperationConfig.md) | One entry per operation the step&#39;s connector handles. | 
**order** | **int** | Execution order among the workflow&#39;s steps, lowest first. | 

## Example

```python
from fireblocks.models.step_config import StepConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StepConfig from a JSON string
step_config_instance = StepConfig.from_json(json)
# print the JSON string representation of the object
print(StepConfig.to_json())

# convert the object into a dict
step_config_dict = step_config_instance.to_dict()
# create an instance of StepConfig from a dict
step_config_from_dict = StepConfig.from_dict(step_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


