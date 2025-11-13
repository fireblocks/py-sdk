# USWireDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**USWireAddress**](USWireAddress.md) |  | 

## Example

```python
from fireblocks.models.us_wire_destination import USWireDestination

# TODO update the JSON string below
json = "{}"
# create an instance of USWireDestination from a JSON string
us_wire_destination_instance = USWireDestination.from_json(json)
# print the JSON string representation of the object
print(USWireDestination.to_json())

# convert the object into a dict
us_wire_destination_dict = us_wire_destination_instance.to_dict()
# create an instance of USWireDestination from a dict
us_wire_destination_from_dict = USWireDestination.from_dict(us_wire_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


