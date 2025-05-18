# ReadCallFunctionDtoAbiFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_mutability** | **str** |  | 
**outputs** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**name** | **str** | The name of the instruction | 
**type** | **str** |  | 
**inputs** | [**List[ParameterWithValue]**](ParameterWithValue.md) |  | 
**description** | **str** |  | [optional] 
**discriminator** | **List[float]** | The discriminator for the instruction. Acts as a function selector | 
**accounts** | [**List[SOLAccountWithValue]**](SOLAccountWithValue.md) |  | 
**args** | [**List[SolParameterWithValue]**](SolParameterWithValue.md) | The arguments of the instruction | 

## Example

```python
from fireblocks.models.read_call_function_dto_abi_function import ReadCallFunctionDtoAbiFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ReadCallFunctionDtoAbiFunction from a JSON string
read_call_function_dto_abi_function_instance = ReadCallFunctionDtoAbiFunction.from_json(json)
# print the JSON string representation of the object
print(ReadCallFunctionDtoAbiFunction.to_json())

# convert the object into a dict
read_call_function_dto_abi_function_dict = read_call_function_dto_abi_function_instance.to_dict()
# create an instance of ReadCallFunctionDtoAbiFunction from a dict
read_call_function_dto_abi_function_from_dict = ReadCallFunctionDtoAbiFunction.from_dict(read_call_function_dto_abi_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


