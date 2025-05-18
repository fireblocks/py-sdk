# ReadCallFunctionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abi_function** | [**ReadCallFunctionDtoAbiFunction**](ReadCallFunctionDtoAbiFunction.md) |  | 

## Example

```python
from fireblocks.models.read_call_function_dto import ReadCallFunctionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReadCallFunctionDto from a JSON string
read_call_function_dto_instance = ReadCallFunctionDto.from_json(json)
# print the JSON string representation of the object
print(ReadCallFunctionDto.to_json())

# convert the object into a dict
read_call_function_dto_dict = read_call_function_dto_instance.to_dict()
# create an instance of ReadCallFunctionDto from a dict
read_call_function_dto_from_dict = ReadCallFunctionDto.from_dict(read_call_function_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


