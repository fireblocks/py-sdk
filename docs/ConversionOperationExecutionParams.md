# ConversionOperationExecutionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_operation_id** | **str** |  | 
**execution_params** | [**ConversionOperationExecutionParamsExecutionParams**](ConversionOperationExecutionParamsExecutionParams.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.conversion_operation_execution_params import ConversionOperationExecutionParams

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionOperationExecutionParams from a JSON string
conversion_operation_execution_params_instance = ConversionOperationExecutionParams.from_json(json)
# print the JSON string representation of the object
print ConversionOperationExecutionParams.to_json()

# convert the object into a dict
conversion_operation_execution_params_dict = conversion_operation_execution_params_instance.to_dict()
# create an instance of ConversionOperationExecutionParams from a dict
conversion_operation_execution_params_form_dict = conversion_operation_execution_params.from_dict(conversion_operation_execution_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


