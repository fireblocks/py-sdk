# TransferOperationExecutionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**AssetAmount**](AssetAmount.md) |  | 
**fee** | [**AssetAmount**](AssetAmount.md) |  | 

## Example

```python
from fireblocks.models.transfer_operation_execution_output import TransferOperationExecutionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOperationExecutionOutput from a JSON string
transfer_operation_execution_output_instance = TransferOperationExecutionOutput.from_json(json)
# print the JSON string representation of the object
print(TransferOperationExecutionOutput.to_json())

# convert the object into a dict
transfer_operation_execution_output_dict = transfer_operation_execution_output_instance.to_dict()
# create an instance of TransferOperationExecutionOutput from a dict
transfer_operation_execution_output_from_dict = TransferOperationExecutionOutput.from_dict(transfer_operation_execution_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


