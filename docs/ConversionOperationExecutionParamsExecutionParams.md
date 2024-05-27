# ConversionOperationExecutionParamsExecutionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**src_asset_id** | **str** |  | [optional] 
**dest_asset_id** | **str** |  | [optional] 
**slippage_basis_points** | **int** |  | [optional] 

## Example

```python
from fireblocks_client.models.conversion_operation_execution_params_execution_params import ConversionOperationExecutionParamsExecutionParams

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionOperationExecutionParamsExecutionParams from a JSON string
conversion_operation_execution_params_execution_params_instance = ConversionOperationExecutionParamsExecutionParams.from_json(json)
# print the JSON string representation of the object
print ConversionOperationExecutionParamsExecutionParams.to_json()

# convert the object into a dict
conversion_operation_execution_params_execution_params_dict = conversion_operation_execution_params_execution_params_instance.to_dict()
# create an instance of ConversionOperationExecutionParamsExecutionParams from a dict
conversion_operation_execution_params_execution_params_form_dict = conversion_operation_execution_params_execution_params.from_dict(conversion_operation_execution_params_execution_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


