# TransferOperationPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**TransferOperationConfigParams**](TransferOperationConfigParams.md) |  | 
**output** | [**TransferOperationPreviewOutput**](TransferOperationPreviewOutput.md) |  | [optional] 
**failure** | [**TransferOperationFailure**](TransferOperationFailure.md) |  | [optional] 

## Example

```python
from fireblocks.models.transfer_operation_preview import TransferOperationPreview

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOperationPreview from a JSON string
transfer_operation_preview_instance = TransferOperationPreview.from_json(json)
# print the JSON string representation of the object
print(TransferOperationPreview.to_json())

# convert the object into a dict
transfer_operation_preview_dict = transfer_operation_preview_instance.to_dict()
# create an instance of TransferOperationPreview from a dict
transfer_operation_preview_from_dict = TransferOperationPreview.from_dict(transfer_operation_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


