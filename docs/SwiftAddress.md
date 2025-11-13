# SwiftAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**swift_code** | **str** |  | 
**routing_number** | **str** | Routing number identifying the bank account. | 

## Example

```python
from fireblocks.models.swift_address import SwiftAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SwiftAddress from a JSON string
swift_address_instance = SwiftAddress.from_json(json)
# print the JSON string representation of the object
print(SwiftAddress.to_json())

# convert the object into a dict
swift_address_dict = swift_address_instance.to_dict()
# create an instance of SwiftAddress from a dict
swift_address_from_dict = SwiftAddress.from_dict(swift_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


