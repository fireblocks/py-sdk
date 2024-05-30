# UserGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**member_ids** | **List[str]** |  | [optional] 

## Example

```python
from fireblocks.models.user_group_response import UserGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupResponse from a JSON string
user_group_response_instance = UserGroupResponse.from_json(json)
# print the JSON string representation of the object
print(UserGroupResponse.to_json())

# convert the object into a dict
user_group_response_dict = user_group_response_instance.to_dict()
# create an instance of UserGroupResponse from a dict
user_group_response_from_dict = UserGroupResponse.from_dict(user_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


