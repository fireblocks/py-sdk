# GetAutomationSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**List[AutomationSettingsResponse]**](AutomationSettingsResponse.md) | The deposit automations configured for the vault account. | 

## Example

```python
from fireblocks.models.get_automation_settings_response import GetAutomationSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAutomationSettingsResponse from a JSON string
get_automation_settings_response_instance = GetAutomationSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAutomationSettingsResponse.to_json())

# convert the object into a dict
get_automation_settings_response_dict = get_automation_settings_response_instance.to_dict()
# create an instance of GetAutomationSettingsResponse from a dict
get_automation_settings_response_from_dict = GetAutomationSettingsResponse.from_dict(get_automation_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


