# AutomationSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automation_id** | **str** | The ID of this deposit automation. | 
**vault_account_id** | **str** | The vault account this deposit automation applies to. | 
**asset_id** | **str** | The Fireblocks asset ID this automation applies to, if scoped to one. | [optional] 
**automation_type** | **str** | The type of this automation. | 
**time_based** | [**TimeBasedTrigger**](TimeBasedTrigger.md) |  | 

## Example

```python
from fireblocks.models.automation_settings_response import AutomationSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationSettingsResponse from a JSON string
automation_settings_response_instance = AutomationSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(AutomationSettingsResponse.to_json())

# convert the object into a dict
automation_settings_response_dict = automation_settings_response_instance.to_dict()
# create an instance of AutomationSettingsResponse from a dict
automation_settings_response_from_dict = AutomationSettingsResponse.from_dict(automation_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


