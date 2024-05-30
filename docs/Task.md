# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**job_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**created** | **float** |  | [optional] 
**updated** | **float** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


