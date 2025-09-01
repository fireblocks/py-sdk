# ProgramCallConfig

Program call configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_solana_program_calls** | **str** | Whether Solana program calls are allowed | 

## Example

```python
from fireblocks.models.program_call_config import ProgramCallConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramCallConfig from a JSON string
program_call_config_instance = ProgramCallConfig.from_json(json)
# print the JSON string representation of the object
print(ProgramCallConfig.to_json())

# convert the object into a dict
program_call_config_dict = program_call_config_instance.to_dict()
# create an instance of ProgramCallConfig from a dict
program_call_config_from_dict = ProgramCallConfig.from_dict(program_call_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


