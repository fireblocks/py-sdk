# SpeiDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**SpeiAddress**](SpeiAddress.md) |  | 

## Example

```python
from fireblocks.models.spei_destination import SpeiDestination

# TODO update the JSON string below
json = "{}"
# create an instance of SpeiDestination from a JSON string
spei_destination_instance = SpeiDestination.from_json(json)
# print the JSON string representation of the object
print(SpeiDestination.to_json())

# convert the object into a dict
spei_destination_dict = spei_destination_instance.to_dict()
# create an instance of SpeiDestination from a dict
spei_destination_from_dict = SpeiDestination.from_dict(spei_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


