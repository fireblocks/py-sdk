# FpsUkDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transfer rail type for the destination | 
**address** | [**FpsUkAddress**](FpsUkAddress.md) |  | 

## Example

```python
from fireblocks.models.fps_uk_destination import FpsUkDestination

# TODO update the JSON string below
json = "{}"
# create an instance of FpsUkDestination from a JSON string
fps_uk_destination_instance = FpsUkDestination.from_json(json)
# print the JSON string representation of the object
print(FpsUkDestination.to_json())

# convert the object into a dict
fps_uk_destination_dict = fps_uk_destination_instance.to_dict()
# create an instance of FpsUkDestination from a dict
fps_uk_destination_from_dict = FpsUkDestination.from_dict(fps_uk_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


