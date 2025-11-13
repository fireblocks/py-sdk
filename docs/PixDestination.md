# PixDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**PixAddress**](PixAddress.md) |  | 

## Example

```python
from fireblocks.models.pix_destination import PixDestination

# TODO update the JSON string below
json = "{}"
# create an instance of PixDestination from a JSON string
pix_destination_instance = PixDestination.from_json(json)
# print the JSON string representation of the object
print(PixDestination.to_json())

# convert the object into a dict
pix_destination_dict = pix_destination_instance.to_dict()
# create an instance of PixDestination from a dict
pix_destination_from_dict = PixDestination.from_dict(pix_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


