# TransferOperationExecutionParamsExecutionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**source** | [**Account**](Account.md) |  | [optional] 
**destination** | [**Destination**](Destination.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.transfer_operation_execution_params_execution_params import TransferOperationExecutionParamsExecutionParams

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOperationExecutionParamsExecutionParams from a JSON string
transfer_operation_execution_params_execution_params_instance = TransferOperationExecutionParamsExecutionParams.from_json(json)
# print the JSON string representation of the object
print(TransferOperationExecutionParamsExecutionParams.to_json())

# convert the object into a dict
transfer_operation_execution_params_execution_params_dict = transfer_operation_execution_params_execution_params_instance.to_dict()
# create an instance of TransferOperationExecutionParamsExecutionParams from a dict
transfer_operation_execution_params_execution_params_from_dict = TransferOperationExecutionParamsExecutionParams.from_dict(transfer_operation_execution_params_execution_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


