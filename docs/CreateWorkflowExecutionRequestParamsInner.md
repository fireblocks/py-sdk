# CreateWorkflowExecutionRequestParamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_operation_id** | **str** |  | 
**execution_params** | [**DisbursementOperationExecutionParamsExecutionParams**](DisbursementOperationExecutionParamsExecutionParams.md) |  | [optional] 

## Example

```python
from fireblocks.models.create_workflow_execution_request_params_inner import CreateWorkflowExecutionRequestParamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkflowExecutionRequestParamsInner from a JSON string
create_workflow_execution_request_params_inner_instance = CreateWorkflowExecutionRequestParamsInner.from_json(json)
# print the JSON string representation of the object
print(CreateWorkflowExecutionRequestParamsInner.to_json())

# convert the object into a dict
create_workflow_execution_request_params_inner_dict = create_workflow_execution_request_params_inner_instance.to_dict()
# create an instance of CreateWorkflowExecutionRequestParamsInner from a dict
create_workflow_execution_request_params_inner_from_dict = CreateWorkflowExecutionRequestParamsInner.from_dict(create_workflow_execution_request_params_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


