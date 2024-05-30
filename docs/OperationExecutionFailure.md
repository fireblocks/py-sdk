# OperationExecutionFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from fireblocks_client.models.operation_execution_failure import OperationExecutionFailure

# TODO update the JSON string below
json = "{}"
# create an instance of OperationExecutionFailure from a JSON string
operation_execution_failure_instance = OperationExecutionFailure.from_json(json)
# print the JSON string representation of the object
print(OperationExecutionFailure.to_json())

# convert the object into a dict
operation_execution_failure_dict = operation_execution_failure_instance.to_dict()
# create an instance of OperationExecutionFailure from a dict
operation_execution_failure_from_dict = OperationExecutionFailure.from_dict(operation_execution_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


