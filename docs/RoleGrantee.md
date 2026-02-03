# RoleGrantee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_address** | **str** | The address of the account that has been granted the role | 
**date_of_grant** | **datetime** | The date when the role was granted to this account | 

## Example

```python
from fireblocks.models.role_grantee import RoleGrantee

# TODO update the JSON string below
json = "{}"
# create an instance of RoleGrantee from a JSON string
role_grantee_instance = RoleGrantee.from_json(json)
# print the JSON string representation of the object
print(RoleGrantee.to_json())

# convert the object into a dict
role_grantee_dict = role_grantee_instance.to_dict()
# create an instance of RoleGrantee from a dict
role_grantee_from_dict = RoleGrantee.from_dict(role_grantee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


