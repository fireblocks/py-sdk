# DirectAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates this uses direct provider access | 
**provider_id** | **str** | The ID of the provider | 

## Example

```python
from fireblocks.models.direct_access import DirectAccess

# TODO update the JSON string below
json = "{}"
# create an instance of DirectAccess from a JSON string
direct_access_instance = DirectAccess.from_json(json)
# print the JSON string representation of the object
print(DirectAccess.to_json())

# convert the object into a dict
direct_access_dict = direct_access_instance.to_dict()
# create an instance of DirectAccess from a dict
direct_access_from_dict = DirectAccess.from_dict(direct_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


