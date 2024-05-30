# TransferOperationExecutionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_operation_id** | **str** |  | 
**execution_params** | [**TransferOperationExecutionParamsExecutionParams**](TransferOperationExecutionParamsExecutionParams.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.transfer_operation_execution_params import TransferOperationExecutionParams

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOperationExecutionParams from a JSON string
transfer_operation_execution_params_instance = TransferOperationExecutionParams.from_json(json)
# print the JSON string representation of the object
print(TransferOperationExecutionParams.to_json())

# convert the object into a dict
transfer_operation_execution_params_dict = transfer_operation_execution_params_instance.to_dict()
# create an instance of TransferOperationExecutionParams from a dict
transfer_operation_execution_params_from_dict = TransferOperationExecutionParams.from_dict(transfer_operation_execution_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


