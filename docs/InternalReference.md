# InternalReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PeerType**](PeerType.md) |  | 
**account_id** | **str** |  | 

## Example

```python
from fireblocks.models.internal_reference import InternalReference

# TODO update the JSON string below
json = "{}"
# create an instance of InternalReference from a JSON string
internal_reference_instance = InternalReference.from_json(json)
# print the JSON string representation of the object
print(InternalReference.to_json())

# convert the object into a dict
internal_reference_dict = internal_reference_instance.to_dict()
# create an instance of InternalReference from a dict
internal_reference_from_dict = InternalReference.from_dict(internal_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


