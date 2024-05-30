# CreateUserGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**member_ids** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.create_user_group_response import CreateUserGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserGroupResponse from a JSON string
create_user_group_response_instance = CreateUserGroupResponse.from_json(json)
# print the JSON string representation of the object
print(CreateUserGroupResponse.to_json())

# convert the object into a dict
create_user_group_response_dict = create_user_group_response_instance.to_dict()
# create an instance of CreateUserGroupResponse from a dict
create_user_group_response_from_dict = CreateUserGroupResponse.from_dict(create_user_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


