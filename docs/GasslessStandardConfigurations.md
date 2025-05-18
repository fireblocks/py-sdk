# GasslessStandardConfigurations

The gasless configuration of the contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gasless_standard_configurations** | [**Dict[str, GasslessStandardConfigurationsGaslessStandardConfigurationsValue]**](GasslessStandardConfigurationsGaslessStandardConfigurationsValue.md) |  | [optional] 

## Example

```python
from fireblocks.models.gassless_standard_configurations import GasslessStandardConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of GasslessStandardConfigurations from a JSON string
gassless_standard_configurations_instance = GasslessStandardConfigurations.from_json(json)
# print the JSON string representation of the object
print(GasslessStandardConfigurations.to_json())

# convert the object into a dict
gassless_standard_configurations_dict = gassless_standard_configurations_instance.to_dict()
# create an instance of GasslessStandardConfigurations from a dict
gassless_standard_configurations_from_dict = GasslessStandardConfigurations.from_dict(gassless_standard_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


