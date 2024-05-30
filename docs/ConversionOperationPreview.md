# ConversionOperationPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**ConversionOperationConfigParams**](ConversionOperationConfigParams.md) |  | 
**output** | [**ConversionOperationPreviewOutput**](ConversionOperationPreviewOutput.md) |  | [optional] 
**failure** | [**ConversionOperationFailure**](ConversionOperationFailure.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.conversion_operation_preview import ConversionOperationPreview

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionOperationPreview from a JSON string
conversion_operation_preview_instance = ConversionOperationPreview.from_json(json)
# print the JSON string representation of the object
print(ConversionOperationPreview.to_json())

# convert the object into a dict
conversion_operation_preview_dict = conversion_operation_preview_instance.to_dict()
# create an instance of ConversionOperationPreview from a dict
conversion_operation_preview_from_dict = ConversionOperationPreview.from_dict(conversion_operation_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


