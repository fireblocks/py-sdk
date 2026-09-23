# UpdateWorkflowStatusRequest

Request to change a workflow's status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**WorkflowStatusEnum**](WorkflowStatusEnum.md) |  | 

## Example

```python
from fireblocks.models.update_workflow_status_request import UpdateWorkflowStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowStatusRequest from a JSON string
update_workflow_status_request_instance = UpdateWorkflowStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowStatusRequest.to_json())

# convert the object into a dict
update_workflow_status_request_dict = update_workflow_status_request_instance.to_dict()
# create an instance of UpdateWorkflowStatusRequest from a dict
update_workflow_status_request_from_dict = UpdateWorkflowStatusRequest.from_dict(update_workflow_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


