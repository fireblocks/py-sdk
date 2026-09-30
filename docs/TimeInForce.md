# TimeInForce

Time in force for limit orders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator for the fill-or-kill time-in-force type. | 

## Example

```python
from fireblocks.models.time_in_force import TimeInForce

# TODO update the JSON string below
json = "{}"
# create an instance of TimeInForce from a JSON string
time_in_force_instance = TimeInForce.from_json(json)
# print the JSON string representation of the object
print(TimeInForce.to_json())

# convert the object into a dict
time_in_force_dict = time_in_force_instance.to_dict()
# create an instance of TimeInForce from a dict
time_in_force_from_dict = TimeInForce.from_dict(time_in_force_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


