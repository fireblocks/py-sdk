# ConversionOperationConfigParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**src_asset_id** | **str** |  | [optional] 
**dest_asset_id** | **str** |  | 
**slippage_basis_points** | **int** |  | [optional] 

## Example

```python
from fireblocks.models.conversion_operation_config_params import ConversionOperationConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionOperationConfigParams from a JSON string
conversion_operation_config_params_instance = ConversionOperationConfigParams.from_json(json)
# print the JSON string representation of the object
print(ConversionOperationConfigParams.to_json())

# convert the object into a dict
conversion_operation_config_params_dict = conversion_operation_config_params_instance.to_dict()
# create an instance of ConversionOperationConfigParams from a dict
conversion_operation_config_params_from_dict = ConversionOperationConfigParams.from_dict(conversion_operation_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


