# CreateConsoleUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | users firstName | 
**last_name** | **str** | users lastName | 
**role** | **str** | users role | 
**email** | **str** | valid email address | 

## Example

```python
from fireblocks_client.models.create_console_user import CreateConsoleUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConsoleUser from a JSON string
create_console_user_instance = CreateConsoleUser.from_json(json)
# print the JSON string representation of the object
print CreateConsoleUser.to_json()

# convert the object into a dict
create_console_user_dict = create_console_user_instance.to_dict()
# create an instance of CreateConsoleUser from a dict
create_console_user_form_dict = create_console_user.from_dict(create_console_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


