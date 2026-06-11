# ActiveRolesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_roles** | [**Dict[str, RoleDetails]**](RoleDetails.md) | Active RBAC roles on the contract, keyed by role name (e.g. DEFAULT_ADMIN_ROLE, MINTER_ROLE). Each entry contains the on-chain role hash, a human-readable description, and the list of accounts currently granted that role. | 

## Example

```python
from fireblocks.models.active_roles_response import ActiveRolesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveRolesResponse from a JSON string
active_roles_response_instance = ActiveRolesResponse.from_json(json)
# print the JSON string representation of the object
print(ActiveRolesResponse.to_json())

# convert the object into a dict
active_roles_response_dict = active_roles_response_instance.to_dict()
# create an instance of ActiveRolesResponse from a dict
active_roles_response_from_dict = ActiveRolesResponse.from_dict(active_roles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


