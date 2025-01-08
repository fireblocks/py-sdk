# GetMpcKeysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The workspace id of the keys | 
**keys** | [**List[MpcKey]**](MpcKey.md) | The keys that are associated with the workspace | 

## Example

```python
from fireblocks.models.get_mpc_keys_response import GetMpcKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMpcKeysResponse from a JSON string
get_mpc_keys_response_instance = GetMpcKeysResponse.from_json(json)
# print the JSON string representation of the object
print(GetMpcKeysResponse.to_json())

# convert the object into a dict
get_mpc_keys_response_dict = get_mpc_keys_response_instance.to_dict()
# create an instance of GetMpcKeysResponse from a dict
get_mpc_keys_response_from_dict = GetMpcKeysResponse.from_dict(get_mpc_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


