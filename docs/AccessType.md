# AccessType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates this uses account-based access | 
**provider_id** | **str** | The ID of the provider | 
**account_id** | **str** | The ID of the account | 

## Example

```python
from fireblocks.models.access_type import AccessType

# TODO update the JSON string below
json = "{}"
# create an instance of AccessType from a JSON string
access_type_instance = AccessType.from_json(json)
# print the JSON string representation of the object
print(AccessType.to_json())

# convert the object into a dict
access_type_dict = access_type_instance.to_dict()
# create an instance of AccessType from a dict
access_type_from_dict = AccessType.from_dict(access_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


