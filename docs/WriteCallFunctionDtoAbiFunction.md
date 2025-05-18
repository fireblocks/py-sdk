# WriteCallFunctionDtoAbiFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_mutability** | **str** |  | 
**outputs** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**type** | **str** |  | 
**name** | **str** | The name of the instruction | 
**inputs** | [**List[ParameterWithValue]**](ParameterWithValue.md) |  | 
**description** | **str** |  | [optional] 
**discriminator** | **List[float]** | The discriminator for the instruction. Acts as a function selector | 
**accounts** | [**List[SOLAccountWithValue]**](SOLAccountWithValue.md) |  | 
**args** | [**List[SolParameterWithValue]**](SolParameterWithValue.md) | The arguments of the instruction | 

## Example

```python
from fireblocks.models.write_call_function_dto_abi_function import WriteCallFunctionDtoAbiFunction

# TODO update the JSON string below
json = "{}"
# create an instance of WriteCallFunctionDtoAbiFunction from a JSON string
write_call_function_dto_abi_function_instance = WriteCallFunctionDtoAbiFunction.from_json(json)
# print the JSON string representation of the object
print(WriteCallFunctionDtoAbiFunction.to_json())

# convert the object into a dict
write_call_function_dto_abi_function_dict = write_call_function_dto_abi_function_instance.to_dict()
# create an instance of WriteCallFunctionDtoAbiFunction from a dict
write_call_function_dto_abi_function_from_dict = WriteCallFunctionDtoAbiFunction.from_dict(write_call_function_dto_abi_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


