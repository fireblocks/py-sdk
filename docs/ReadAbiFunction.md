# ReadAbiFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_mutability** | **str** |  | 
**outputs** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | 
**inputs** | [**List[ParameterWithValue]**](ParameterWithValue.md) |  | 
**description** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.read_abi_function import ReadAbiFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAbiFunction from a JSON string
read_abi_function_instance = ReadAbiFunction.from_json(json)
# print the JSON string representation of the object
print(ReadAbiFunction.to_json())

# convert the object into a dict
read_abi_function_dict = read_abi_function_instance.to_dict()
# create an instance of ReadAbiFunction from a dict
read_abi_function_from_dict = ReadAbiFunction.from_dict(read_abi_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


