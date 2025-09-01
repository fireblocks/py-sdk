# AmountOverTimeConfigRange

Amount range configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **str** | Minimum amount | 
**max** | **str** | Maximum amount (optional) | [optional] 

## Example

```python
from fireblocks.models.amount_over_time_config_range import AmountOverTimeConfigRange

# TODO update the JSON string below
json = "{}"
# create an instance of AmountOverTimeConfigRange from a JSON string
amount_over_time_config_range_instance = AmountOverTimeConfigRange.from_json(json)
# print the JSON string representation of the object
print(AmountOverTimeConfigRange.to_json())

# convert the object into a dict
amount_over_time_config_range_dict = amount_over_time_config_range_instance.to_dict()
# create an instance of AmountOverTimeConfigRange from a dict
amount_over_time_config_range_from_dict = AmountOverTimeConfigRange.from_dict(amount_over_time_config_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


