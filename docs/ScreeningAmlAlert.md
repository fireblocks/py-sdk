# ScreeningAmlAlert

AML alert information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_level** | [**AlertLevelEnum**](AlertLevelEnum.md) |  | 
**alert_name** | **str** | Name or type of the alert | [optional] 
**category** | **str** | Alert category | [optional] 
**service** | **str** | Service that generated the alert | [optional] 
**external_id** | **str** | External identifier for the alert | 
**alert_amount** | **float** | Amount associated with the alert | 
**exposure_type** | [**ScreeningAlertExposureTypeEnum**](ScreeningAlertExposureTypeEnum.md) |  | 
**policy_action** | **str** | Recommended action based on policy | [optional] 
**category_id** | **float** | Category identifier | [optional] 

## Example

```python
from fireblocks.models.screening_aml_alert import ScreeningAmlAlert

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningAmlAlert from a JSON string
screening_aml_alert_instance = ScreeningAmlAlert.from_json(json)
# print the JSON string representation of the object
print(ScreeningAmlAlert.to_json())

# convert the object into a dict
screening_aml_alert_dict = screening_aml_alert_instance.to_dict()
# create an instance of ScreeningAmlAlert from a dict
screening_aml_alert_from_dict = ScreeningAmlAlert.from_dict(screening_aml_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


