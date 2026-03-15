# ChapsDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**ChapsAddress**](ChapsAddress.md) |  | 

## Example

```python
from fireblocks.models.chaps_destination import ChapsDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ChapsDestination from a JSON string
chaps_destination_instance = ChapsDestination.from_json(json)
# print the JSON string representation of the object
print(ChapsDestination.to_json())

# convert the object into a dict
chaps_destination_dict = chaps_destination_instance.to_dict()
# create an instance of ChapsDestination from a dict
chaps_destination_from_dict = ChapsDestination.from_dict(chaps_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


