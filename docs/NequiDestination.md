# NequiDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transfer rail type for the destination | 
**address** | [**NequiAddress**](NequiAddress.md) |  | 

## Example

```python
from fireblocks.models.nequi_destination import NequiDestination

# TODO update the JSON string below
json = "{}"
# create an instance of NequiDestination from a JSON string
nequi_destination_instance = NequiDestination.from_json(json)
# print the JSON string representation of the object
print(NequiDestination.to_json())

# convert the object into a dict
nequi_destination_dict = nequi_destination_instance.to_dict()
# create an instance of NequiDestination from a dict
nequi_destination_from_dict = NequiDestination.from_dict(nequi_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


