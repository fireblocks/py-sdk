# GetWorkflowResponse

A workflow's current definition, including its steps and each step's rule sets.  A workflow is the configuration a screening runs against: an ordered list of steps, each backed by one connector. It must be `ACTIVE` before a screening will accept it — `DRAFT` is the editing state, so a screening never runs against a half-finished configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | Unique identifier of the workflow. | 
**template_id** | **str** | The template this workflow was provisioned from, if any. | [optional] 
**status** | [**WorkflowStatusEnum**](WorkflowStatusEnum.md) |  | 
**title** | **str** | User-facing display name for the workflow. | 
**description** | **str** | User-facing free-text description of the workflow&#39;s purpose. | [optional] 
**created_at** | **str** | Unix timestamp in seconds when the workflow was provisioned, encoded as a string. | 
**steps** | [**List[StepConfig]**](StepConfig.md) | Flat list — one step per connector. | 

## Example

```python
from fireblocks.models.get_workflow_response import GetWorkflowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkflowResponse from a JSON string
get_workflow_response_instance = GetWorkflowResponse.from_json(json)
# print the JSON string representation of the object
print(GetWorkflowResponse.to_json())

# convert the object into a dict
get_workflow_response_dict = get_workflow_response_instance.to_dict()
# create an instance of GetWorkflowResponse from a dict
get_workflow_response_from_dict = GetWorkflowResponse.from_dict(get_workflow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


