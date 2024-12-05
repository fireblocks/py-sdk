# ScreeningUpdateConfigurations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_bypass** | **bool** | Flag to enable or disable bypass screening on tenant configuration. | [optional] 
**disable_unfreeze** | **bool** | Flag to enable or disable unfreeze of transaction frozen by policy rule on tenant configuration. | [optional] 

## Example

```python
from fireblocks.models.screening_update_configurations import ScreeningUpdateConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningUpdateConfigurations from a JSON string
screening_update_configurations_instance = ScreeningUpdateConfigurations.from_json(json)
# print the JSON string representation of the object
print(ScreeningUpdateConfigurations.to_json())

# convert the object into a dict
screening_update_configurations_dict = screening_update_configurations_instance.to_dict()
# create an instance of ScreeningUpdateConfigurations from a dict
screening_update_configurations_from_dict = ScreeningUpdateConfigurations.from_dict(screening_update_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


