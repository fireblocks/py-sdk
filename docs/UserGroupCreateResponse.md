# UserGroupCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**member_ids** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.user_group_create_response import UserGroupCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupCreateResponse from a JSON string
user_group_create_response_instance = UserGroupCreateResponse.from_json(json)
# print the JSON string representation of the object
print UserGroupCreateResponse.to_json()

# convert the object into a dict
user_group_create_response_dict = user_group_create_response_instance.to_dict()
# create an instance of UserGroupCreateResponse from a dict
user_group_create_response_form_dict = user_group_create_response.from_dict(user_group_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


