# AchDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**AchAddress**](AchAddress.md) |  | 

## Example

```python
from fireblocks.models.ach_destination import AchDestination

# TODO update the JSON string below
json = "{}"
# create an instance of AchDestination from a JSON string
ach_destination_instance = AchDestination.from_json(json)
# print the JSON string representation of the object
print(AchDestination.to_json())

# convert the object into a dict
ach_destination_dict = ach_destination_instance.to_dict()
# create an instance of AchDestination from a dict
ach_destination_from_dict = AchDestination.from_dict(ach_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


