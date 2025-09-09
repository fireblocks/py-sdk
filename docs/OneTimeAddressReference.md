# OneTimeAddressReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | **str** |  | 
**tag** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.one_time_address_reference import OneTimeAddressReference

# TODO update the JSON string below
json = "{}"
# create an instance of OneTimeAddressReference from a JSON string
one_time_address_reference_instance = OneTimeAddressReference.from_json(json)
# print the JSON string representation of the object
print(OneTimeAddressReference.to_json())

# convert the object into a dict
one_time_address_reference_dict = one_time_address_reference_instance.to_dict()
# create an instance of OneTimeAddressReference from a dict
one_time_address_reference_from_dict = OneTimeAddressReference.from_dict(one_time_address_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


