# GetAPIUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[APIUser]**](APIUser.md) |  | 

## Example

```python
from fireblocks.models.get_api_users_response import GetAPIUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAPIUsersResponse from a JSON string
get_api_users_response_instance = GetAPIUsersResponse.from_json(json)
# print the JSON string representation of the object
print(GetAPIUsersResponse.to_json())

# convert the object into a dict
get_api_users_response_dict = get_api_users_response_instance.to_dict()
# create an instance of GetAPIUsersResponse from a dict
get_api_users_response_from_dict = GetAPIUsersResponse.from_dict(get_api_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


