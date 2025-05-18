# SolParameterWithValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the parameter | 
**name** | **str** | The name of the parameter | 
**type** | [**IdlType**](IdlType.md) |  | 

## Example

```python
from fireblocks.models.sol_parameter_with_value import SolParameterWithValue

# TODO update the JSON string below
json = "{}"
# create an instance of SolParameterWithValue from a JSON string
sol_parameter_with_value_instance = SolParameterWithValue.from_json(json)
# print the JSON string representation of the object
print(SolParameterWithValue.to_json())

# convert the object into a dict
sol_parameter_with_value_dict = sol_parameter_with_value_instance.to_dict()
# create an instance of SolParameterWithValue from a dict
sol_parameter_with_value_from_dict = SolParameterWithValue.from_dict(sol_parameter_with_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


