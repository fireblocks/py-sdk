# UpdateAutomationSettingsRequest

Request body for changing an existing USDC Gateway deposit automation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_based** | [**TimeBasedTrigger**](TimeBasedTrigger.md) |  | 

## Example

```python
from fireblocks.models.update_automation_settings_request import UpdateAutomationSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutomationSettingsRequest from a JSON string
update_automation_settings_request_instance = UpdateAutomationSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAutomationSettingsRequest.to_json())

# convert the object into a dict
update_automation_settings_request_dict = update_automation_settings_request_instance.to_dict()
# create an instance of UpdateAutomationSettingsRequest from a dict
update_automation_settings_request_from_dict = UpdateAutomationSettingsRequest.from_dict(update_automation_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


