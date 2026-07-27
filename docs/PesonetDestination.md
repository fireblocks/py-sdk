# PesonetDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transfer rail type for the destination | 
**address** | [**PesonetAddress**](PesonetAddress.md) |  | 

## Example

```python
from fireblocks.models.pesonet_destination import PesonetDestination

# TODO update the JSON string below
json = "{}"
# create an instance of PesonetDestination from a JSON string
pesonet_destination_instance = PesonetDestination.from_json(json)
# print the JSON string representation of the object
print(PesonetDestination.to_json())

# convert the object into a dict
pesonet_destination_dict = pesonet_destination_instance.to_dict()
# create an instance of PesonetDestination from a dict
pesonet_destination_from_dict = PesonetDestination.from_dict(pesonet_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


