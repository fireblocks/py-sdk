# TimeBasedTrigger

The schedule for this deposit automation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval_value** | **int** | How often the deposit runs, in units of intervalUnit. | 
**interval_unit** | **str** | The unit for intervalValue. | 
**balance_threshold** | **str** | Minimum USDC balance required before a deposit runs. Set to \&quot;0\&quot; to sweep the full available balance every time, with no minimum. | 

## Example

```python
from fireblocks.models.time_based_trigger import TimeBasedTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of TimeBasedTrigger from a JSON string
time_based_trigger_instance = TimeBasedTrigger.from_json(json)
# print the JSON string representation of the object
print(TimeBasedTrigger.to_json())

# convert the object into a dict
time_based_trigger_dict = time_based_trigger_instance.to_dict()
# create an instance of TimeBasedTrigger from a dict
time_based_trigger_from_dict = TimeBasedTrigger.from_dict(time_based_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


