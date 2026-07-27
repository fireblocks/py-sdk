# FpsHkDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transfer rail type for the destination | 
**address** | [**FpsHkAddress**](FpsHkAddress.md) |  | 

## Example

```python
from fireblocks.models.fps_hk_destination import FpsHkDestination

# TODO update the JSON string below
json = "{}"
# create an instance of FpsHkDestination from a JSON string
fps_hk_destination_instance = FpsHkDestination.from_json(json)
# print the JSON string representation of the object
print(FpsHkDestination.to_json())

# convert the object into a dict
fps_hk_destination_dict = fps_hk_destination_instance.to_dict()
# create an instance of FpsHkDestination from a dict
fps_hk_destination_from_dict = FpsHkDestination.from_dict(fps_hk_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


