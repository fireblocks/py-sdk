# LeanAbiFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The function name | [optional] 
**inputs** | [**List[ParameterWithValue]**](ParameterWithValue.md) | The function inputs | 

## Example

```python
from fireblocks.models.lean_abi_function import LeanAbiFunction

# TODO update the JSON string below
json = "{}"
# create an instance of LeanAbiFunction from a JSON string
lean_abi_function_instance = LeanAbiFunction.from_json(json)
# print the JSON string representation of the object
print(LeanAbiFunction.to_json())

# convert the object into a dict
lean_abi_function_dict = lean_abi_function_instance.to_dict()
# create an instance of LeanAbiFunction from a dict
lean_abi_function_from_dict = LeanAbiFunction.from_dict(lean_abi_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


