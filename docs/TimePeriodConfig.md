# TimePeriodConfig

Time period configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **str** | Time period in seconds | 
**initiator** | [**TimePeriodMatchType**](TimePeriodMatchType.md) |  | 
**source** | [**TimePeriodMatchType**](TimePeriodMatchType.md) |  | 
**destination** | [**TimePeriodMatchType**](TimePeriodMatchType.md) |  | 

## Example

```python
from fireblocks.models.time_period_config import TimePeriodConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodConfig from a JSON string
time_period_config_instance = TimePeriodConfig.from_json(json)
# print the JSON string representation of the object
print(TimePeriodConfig.to_json())

# convert the object into a dict
time_period_config_dict = time_period_config_instance.to_dict()
# create an instance of TimePeriodConfig from a dict
time_period_config_from_dict = TimePeriodConfig.from_dict(time_period_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


