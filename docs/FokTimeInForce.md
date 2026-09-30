# FokTimeInForce

Fill-or-kill - the order must be filled in full at the limit price immediately, or not at all.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator for the fill-or-kill time-in-force type. | 

## Example

```python
from fireblocks.models.fok_time_in_force import FokTimeInForce

# TODO update the JSON string below
json = "{}"
# create an instance of FokTimeInForce from a JSON string
fok_time_in_force_instance = FokTimeInForce.from_json(json)
# print the JSON string representation of the object
print(FokTimeInForce.to_json())

# convert the object into a dict
fok_time_in_force_dict = fok_time_in_force_instance.to_dict()
# create an instance of FokTimeInForce from a dict
fok_time_in_force_from_dict = FokTimeInForce.from_dict(fok_time_in_force_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


