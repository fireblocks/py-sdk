# AutomationSettingsRequest

Request body for setting up a USDC Gateway deposit automation for a vault account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automation_type** | **str** | The type of automation to configure. | 
**asset_id** | **str** | The Fireblocks asset ID this automation applies to. Omit to cover all supported USDC Gateway assets. | [optional] 
**time_based** | [**TimeBasedTrigger**](TimeBasedTrigger.md) |  | 

## Example

```python
from fireblocks.models.automation_settings_request import AutomationSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationSettingsRequest from a JSON string
automation_settings_request_instance = AutomationSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(AutomationSettingsRequest.to_json())

# convert the object into a dict
automation_settings_request_dict = automation_settings_request_instance.to_dict()
# create an instance of AutomationSettingsRequest from a dict
automation_settings_request_from_dict = AutomationSettingsRequest.from_dict(automation_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


