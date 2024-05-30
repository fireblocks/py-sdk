# UserGroupCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | [optional] 
**member_ids** | **List[str]** |  | [optional] 

## Example

```python
from fireblocks_client.models.user_group_create_request import UserGroupCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupCreateRequest from a JSON string
user_group_create_request_instance = UserGroupCreateRequest.from_json(json)
# print the JSON string representation of the object
print(UserGroupCreateRequest.to_json())

# convert the object into a dict
user_group_create_request_dict = user_group_create_request_instance.to_dict()
# create an instance of UserGroupCreateRequest from a dict
user_group_create_request_from_dict = UserGroupCreateRequest.from_dict(user_group_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


