# AddressNotAvailableError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Conflict error message | 
**code** | **float** | Error code | 

## Example

```python
from fireblocks.models.address_not_available_error import AddressNotAvailableError

# TODO update the JSON string below
json = "{}"
# create an instance of AddressNotAvailableError from a JSON string
address_not_available_error_instance = AddressNotAvailableError.from_json(json)
# print the JSON string representation of the object
print(AddressNotAvailableError.to_json())

# convert the object into a dict
address_not_available_error_dict = address_not_available_error_instance.to_dict()
# create an instance of AddressNotAvailableError from a dict
address_not_available_error_from_dict = AddressNotAvailableError.from_dict(address_not_available_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


