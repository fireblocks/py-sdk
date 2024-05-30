# ParameterWithValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the parameter as it appears in the ABI | 
**description** | **str** | A description of the parameter, fetched from the devdoc of this contract | [optional] 
**internal_type** | **str** | The  internal type of the parameter as it appears in the ABI | [optional] 
**type** | **str** | The type of the parameter as it appears in the ABI | 
**components** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**value** | **str** | The value of the parameter. can also be ParameterWithValue | [optional] 
**function_value** | [**LeanAbiFunction**](LeanAbiFunction.md) | The function value of this param (if has one). If this is set, the &#x60;value&#x60; shouldn&#x60;t be. Used for proxies | [optional] 

## Example

```python
from fireblocks_client.models.parameter_with_value import ParameterWithValue

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterWithValue from a JSON string
parameter_with_value_instance = ParameterWithValue.from_json(json)
# print the JSON string representation of the object
print(ParameterWithValue.to_json())

# convert the object into a dict
parameter_with_value_dict = parameter_with_value_instance.to_dict()
# create an instance of ParameterWithValue from a dict
parameter_with_value_from_dict = ParameterWithValue.from_dict(parameter_with_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


