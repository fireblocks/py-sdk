# RoleDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_hash** | **str** | The role hash identifier | 
**description** | **str** | Human-readable description of the role | 
**accounts** | [**List[RoleGrantee]**](RoleGrantee.md) | List of accounts that have been granted this role | 

## Example

```python
from fireblocks.models.role_details import RoleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RoleDetails from a JSON string
role_details_instance = RoleDetails.from_json(json)
# print the JSON string representation of the object
print(RoleDetails.to_json())

# convert the object into a dict
role_details_dict = role_details_instance.to_dict()
# create an instance of RoleDetails from a dict
role_details_from_dict = RoleDetails.from_dict(role_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


