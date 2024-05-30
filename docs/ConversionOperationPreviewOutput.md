# ConversionOperationPreviewOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**AssetAmount**](AssetAmount.md) |  | 
**fee** | [**AssetAmount**](AssetAmount.md) |  | 
**conversion_rate** | **str** |  | 
**time_seconds** | **float** |  | 

## Example

```python
from fireblocks.models.conversion_operation_preview_output import ConversionOperationPreviewOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionOperationPreviewOutput from a JSON string
conversion_operation_preview_output_instance = ConversionOperationPreviewOutput.from_json(json)
# print the JSON string representation of the object
print(ConversionOperationPreviewOutput.to_json())

# convert the object into a dict
conversion_operation_preview_output_dict = conversion_operation_preview_output_instance.to_dict()
# create an instance of ConversionOperationPreviewOutput from a dict
conversion_operation_preview_output_from_dict = ConversionOperationPreviewOutput.from_dict(conversion_operation_preview_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


