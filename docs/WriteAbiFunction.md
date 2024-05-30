# WriteAbiFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_mutability** | **str** |  | 
**outputs** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**inputs** | [**List[ParameterWithValue]**](ParameterWithValue.md) |  | 
**description** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.write_abi_function import WriteAbiFunction

# TODO update the JSON string below
json = "{}"
# create an instance of WriteAbiFunction from a JSON string
write_abi_function_instance = WriteAbiFunction.from_json(json)
# print the JSON string representation of the object
print(WriteAbiFunction.to_json())

# convert the object into a dict
write_abi_function_dict = write_abi_function_instance.to_dict()
# create an instance of WriteAbiFunction from a dict
write_abi_function_from_dict = WriteAbiFunction.from_dict(write_abi_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


