# AmountOverTimeConfig

Amount over time configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**AmountRangeMinMax2**](AmountRangeMinMax2.md) |  | 
**currency** | [**PolicyCurrency**](PolicyCurrency.md) |  | 
**time_period** | [**TimePeriodConfig**](TimePeriodConfig.md) |  | 

## Example

```python
from fireblocks.models.amount_over_time_config import AmountOverTimeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AmountOverTimeConfig from a JSON string
amount_over_time_config_instance = AmountOverTimeConfig.from_json(json)
# print the JSON string representation of the object
print(AmountOverTimeConfig.to_json())

# convert the object into a dict
amount_over_time_config_dict = amount_over_time_config_instance.to_dict()
# create an instance of AmountOverTimeConfig from a dict
amount_over_time_config_from_dict = AmountOverTimeConfig.from_dict(amount_over_time_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


