# APIUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the user | [optional] 
**name** | **str** | The name of the user | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**enabled** | **bool** | Whether the user is enabled | [optional] 
**status** | [**UserStatus**](UserStatus.md) |  | [optional] 
**user_type** | [**UserType**](UserType.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.api_user import APIUser

# TODO update the JSON string below
json = "{}"
# create an instance of APIUser from a JSON string
api_user_instance = APIUser.from_json(json)
# print the JSON string representation of the object
print APIUser.to_json()

# convert the object into a dict
api_user_dict = api_user_instance.to_dict()
# create an instance of APIUser from a dict
api_user_form_dict = api_user.from_dict(api_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


