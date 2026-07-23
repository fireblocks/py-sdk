# SaveAutomationSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automation_id** | **str** | The ID of the newly created deposit automation. | 

## Example

```python
from fireblocks.models.save_automation_settings_response import SaveAutomationSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveAutomationSettingsResponse from a JSON string
save_automation_settings_response_instance = SaveAutomationSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(SaveAutomationSettingsResponse.to_json())

# convert the object into a dict
save_automation_settings_response_dict = save_automation_settings_response_instance.to_dict()
# create an instance of SaveAutomationSettingsResponse from a dict
save_automation_settings_response_from_dict = SaveAutomationSettingsResponse.from_dict(save_automation_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


