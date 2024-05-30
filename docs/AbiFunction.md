# AbiFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the contract function as it appears in the ABI | [optional] 
**state_mutability** | **str** | The state mutability of the contract function as it appears in the ABI | [optional] 
**type** | **str** | The type if the function | 
**inputs** | [**List[Parameter]**](Parameter.md) | The parameters that this function/constructor posses | 
**outputs** | [**List[Parameter]**](Parameter.md) | The parameters that this &#39;read&#39; function returns | [optional] 
**description** | **str** | The documentation of this function (if has any) | [optional] 

## Example

```python
from fireblocks.models.abi_function import AbiFunction

# TODO update the JSON string below
json = "{}"
# create an instance of AbiFunction from a JSON string
abi_function_instance = AbiFunction.from_json(json)
# print the JSON string representation of the object
print(AbiFunction.to_json())

# convert the object into a dict
abi_function_dict = abi_function_instance.to_dict()
# create an instance of AbiFunction from a dict
abi_function_from_dict = AbiFunction.from_dict(abi_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


