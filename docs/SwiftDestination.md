# SwiftDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**SwiftAddress**](SwiftAddress.md) |  | 

## Example

```python
from fireblocks.models.swift_destination import SwiftDestination

# TODO update the JSON string below
json = "{}"
# create an instance of SwiftDestination from a JSON string
swift_destination_instance = SwiftDestination.from_json(json)
# print the JSON string representation of the object
print(SwiftDestination.to_json())

# convert the object into a dict
swift_destination_dict = swift_destination_instance.to_dict()
# create an instance of SwiftDestination from a dict
swift_destination_from_dict = SwiftDestination.from_dict(swift_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


