# SolParameter

The arguments of the instruction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the parameter | 
**type** | [**IdlType**](IdlType.md) |  | 

## Example

```python
from fireblocks.models.sol_parameter import SolParameter

# TODO update the JSON string below
json = "{}"
# create an instance of SolParameter from a JSON string
sol_parameter_instance = SolParameter.from_json(json)
# print the JSON string representation of the object
print(SolParameter.to_json())

# convert the object into a dict
sol_parameter_dict = sol_parameter_instance.to_dict()
# create an instance of SolParameter from a dict
sol_parameter_from_dict = SolParameter.from_dict(sol_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


