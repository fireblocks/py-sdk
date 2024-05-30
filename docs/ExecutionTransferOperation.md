# ExecutionTransferOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**status** | [**ExecutionOperationStatus**](ExecutionOperationStatus.md) |  | 
**validation_failure** | [**TransferValidationFailure**](TransferValidationFailure.md) |  | [optional] 
**operation_type** | [**TransferOperationType**](TransferOperationType.md) |  | 
**preview** | [**TransferOperationPreview**](TransferOperationPreview.md) |  | [optional] 
**execution** | [**TransferOperationExecution**](TransferOperationExecution.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.execution_transfer_operation import ExecutionTransferOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionTransferOperation from a JSON string
execution_transfer_operation_instance = ExecutionTransferOperation.from_json(json)
# print the JSON string representation of the object
print(ExecutionTransferOperation.to_json())

# convert the object into a dict
execution_transfer_operation_dict = execution_transfer_operation_instance.to_dict()
# create an instance of ExecutionTransferOperation from a dict
execution_transfer_operation_from_dict = ExecutionTransferOperation.from_dict(execution_transfer_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


