# GetConsoleUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[ConsoleUser]**](ConsoleUser.md) |  | 

## Example

```python
from fireblocks_client.models.get_console_users_response import GetConsoleUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetConsoleUsersResponse from a JSON string
get_console_users_response_instance = GetConsoleUsersResponse.from_json(json)
# print the JSON string representation of the object
print GetConsoleUsersResponse.to_json()

# convert the object into a dict
get_console_users_response_dict = get_console_users_response_instance.to_dict()
# create an instance of GetConsoleUsersResponse from a dict
get_console_users_response_form_dict = get_console_users_response.from_dict(get_console_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


