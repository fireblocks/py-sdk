# ConversionOperationExecutionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**AssetAmount**](AssetAmount.md) |  | 
**fee** | [**AssetAmount**](AssetAmount.md) |  | 
**conversion_rate** | **str** |  | 

## Example

```python
from fireblocks.models.conversion_operation_execution_output import ConversionOperationExecutionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionOperationExecutionOutput from a JSON string
conversion_operation_execution_output_instance = ConversionOperationExecutionOutput.from_json(json)
# print the JSON string representation of the object
print(ConversionOperationExecutionOutput.to_json())

# convert the object into a dict
conversion_operation_execution_output_dict = conversion_operation_execution_output_instance.to_dict()
# create an instance of ConversionOperationExecutionOutput from a dict
conversion_operation_execution_output_from_dict = ConversionOperationExecutionOutput.from_dict(conversion_operation_execution_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


