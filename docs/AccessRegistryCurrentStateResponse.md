# AccessRegistryCurrentStateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccessRegistryAddressItem]**](AccessRegistryAddressItem.md) | Array of active addresses in the access registry | 
**next** | **str** | Cursor for next page | [optional] 
**prev** | **str** | Cursor for previous page | [optional] 
**total** | **float** | Total count of active addresses in the access registry | [optional] 

## Example

```python
from fireblocks.models.access_registry_current_state_response import AccessRegistryCurrentStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRegistryCurrentStateResponse from a JSON string
access_registry_current_state_response_instance = AccessRegistryCurrentStateResponse.from_json(json)
# print the JSON string representation of the object
print(AccessRegistryCurrentStateResponse.to_json())

# convert the object into a dict
access_registry_current_state_response_dict = access_registry_current_state_response_instance.to_dict()
# create an instance of AccessRegistryCurrentStateResponse from a dict
access_registry_current_state_response_from_dict = AccessRegistryCurrentStateResponse.from_dict(access_registry_current_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


