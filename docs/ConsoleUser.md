# ConsoleUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the user | [optional] 
**first_name** | **str** | The first name of the user | [optional] 
**last_name** | **str** | The last name of the user | [optional] 
**email** | **str** | The email address of the user | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**enabled** | **bool** | Whether the user is enabled | [optional] 
**status** | [**UserStatus**](UserStatus.md) |  | [optional] 
**user_type** | [**UserType**](UserType.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.console_user import ConsoleUser

# TODO update the JSON string below
json = "{}"
# create an instance of ConsoleUser from a JSON string
console_user_instance = ConsoleUser.from_json(json)
# print the JSON string representation of the object
print ConsoleUser.to_json()

# convert the object into a dict
console_user_dict = console_user_instance.to_dict()
# create an instance of ConsoleUser from a dict
console_user_form_dict = console_user.from_dict(console_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


