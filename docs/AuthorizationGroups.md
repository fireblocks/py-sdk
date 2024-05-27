# AuthorizationGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**th** | **float** |  | [optional] 
**users** | **Dict[str, str]** |  | [optional] 

## Example

```python
from fireblocks_client.models.authorization_groups import AuthorizationGroups

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationGroups from a JSON string
authorization_groups_instance = AuthorizationGroups.from_json(json)
# print the JSON string representation of the object
print AuthorizationGroups.to_json()

# convert the object into a dict
authorization_groups_dict = authorization_groups_instance.to_dict()
# create an instance of AuthorizationGroups from a dict
authorization_groups_form_dict = authorization_groups.from_dict(authorization_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


