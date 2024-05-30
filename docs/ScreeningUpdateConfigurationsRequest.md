# ScreeningUpdateConfigurationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_bypass** | **bool** | Flag to enable or disable bypass screening on tenant configuration. | [optional] 
**disable_unfreeze** | **bool** | Flag to enable or disable unfreeze of transaction frozen by policy rule on tenant configuration. | [optional] 

## Example

```python
from fireblocks.models.screening_update_configurations_request import ScreeningUpdateConfigurationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningUpdateConfigurationsRequest from a JSON string
screening_update_configurations_request_instance = ScreeningUpdateConfigurationsRequest.from_json(json)
# print the JSON string representation of the object
print(ScreeningUpdateConfigurationsRequest.to_json())

# convert the object into a dict
screening_update_configurations_request_dict = screening_update_configurations_request_instance.to_dict()
# create an instance of ScreeningUpdateConfigurationsRequest from a dict
screening_update_configurations_request_from_dict = ScreeningUpdateConfigurationsRequest.from_dict(screening_update_configurations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


