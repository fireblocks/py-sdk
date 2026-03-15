# InternalTransferDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**InternalTransferAddress**](InternalTransferAddress.md) |  | [optional] 

## Example

```python
from fireblocks.models.internal_transfer_destination import InternalTransferDestination

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransferDestination from a JSON string
internal_transfer_destination_instance = InternalTransferDestination.from_json(json)
# print the JSON string representation of the object
print(InternalTransferDestination.to_json())

# convert the object into a dict
internal_transfer_destination_dict = internal_transfer_destination_instance.to_dict()
# create an instance of InternalTransferDestination from a dict
internal_transfer_destination_from_dict = InternalTransferDestination.from_dict(internal_transfer_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


