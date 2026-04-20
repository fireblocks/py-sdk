# ByorkTimeoutRange

Allowed range for timeout values (seconds). Use when calling PUT config/timeouts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_seconds** | **int** |  | [optional] 
**max_seconds** | **int** |  | [optional] 

## Example

```python
from fireblocks.models.byork_timeout_range import ByorkTimeoutRange

# TODO update the JSON string below
json = "{}"
# create an instance of ByorkTimeoutRange from a JSON string
byork_timeout_range_instance = ByorkTimeoutRange.from_json(json)
# print the JSON string representation of the object
print(ByorkTimeoutRange.to_json())

# convert the object into a dict
byork_timeout_range_dict = byork_timeout_range_instance.to_dict()
# create an instance of ByorkTimeoutRange from a dict
byork_timeout_range_from_dict = ByorkTimeoutRange.from_dict(byork_timeout_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


