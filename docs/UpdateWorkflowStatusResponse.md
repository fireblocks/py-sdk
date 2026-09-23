# UpdateWorkflowStatusResponse

The workflow's status after the update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | Unique identifier of the workflow. | 
**status** | [**WorkflowStatusEnum**](WorkflowStatusEnum.md) |  | 

## Example

```python
from fireblocks.models.update_workflow_status_response import UpdateWorkflowStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowStatusResponse from a JSON string
update_workflow_status_response_instance = UpdateWorkflowStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowStatusResponse.to_json())

# convert the object into a dict
update_workflow_status_response_dict = update_workflow_status_response_instance.to_dict()
# create an instance of UpdateWorkflowStatusResponse from a dict
update_workflow_status_response_from_dict = UpdateWorkflowStatusResponse.from_dict(update_workflow_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


