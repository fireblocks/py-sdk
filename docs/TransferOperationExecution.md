# TransferOperationExecution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**TransferOperationConfigParams**](TransferOperationConfigParams.md) |  | 
**output** | [**TransferOperationExecutionOutput**](TransferOperationExecutionOutput.md) |  | [optional] 
**tx_id** | **str** |  | [optional] 
**started_at** | **float** |  | 
**finished_at** | **float** |  | [optional] 
**failure** | [**TransferOperationFailure**](TransferOperationFailure.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.transfer_operation_execution import TransferOperationExecution

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOperationExecution from a JSON string
transfer_operation_execution_instance = TransferOperationExecution.from_json(json)
# print the JSON string representation of the object
print TransferOperationExecution.to_json()

# convert the object into a dict
transfer_operation_execution_dict = transfer_operation_execution_instance.to_dict()
# create an instance of TransferOperationExecution from a dict
transfer_operation_execution_form_dict = transfer_operation_execution.from_dict(transfer_operation_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


