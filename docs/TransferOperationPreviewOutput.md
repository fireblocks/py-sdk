# TransferOperationPreviewOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**AssetAmount**](AssetAmount.md) |  | 
**fee** | [**AssetAmount**](AssetAmount.md) |  | 
**is_sign_required** | **bool** |  | 
**time_seconds** | **float** |  | 

## Example

```python
from fireblocks_client.models.transfer_operation_preview_output import TransferOperationPreviewOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOperationPreviewOutput from a JSON string
transfer_operation_preview_output_instance = TransferOperationPreviewOutput.from_json(json)
# print the JSON string representation of the object
print(TransferOperationPreviewOutput.to_json())

# convert the object into a dict
transfer_operation_preview_output_dict = transfer_operation_preview_output_instance.to_dict()
# create an instance of TransferOperationPreviewOutput from a dict
transfer_operation_preview_output_from_dict = TransferOperationPreviewOutput.from_dict(transfer_operation_preview_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


