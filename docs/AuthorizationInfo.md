# AuthorizationInfo

The information about your [Transaction Authorization Policy (TAP).](https://developers.fireblocks.com/docs/capabilities#transaction-authorization-policy-tap)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_operator_as_authorizer** | **bool** |  | [optional] 
**logic** | **str** |  | [optional] 
**groups** | [**List[AuthorizationGroups]**](AuthorizationGroups.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.authorization_info import AuthorizationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationInfo from a JSON string
authorization_info_instance = AuthorizationInfo.from_json(json)
# print the JSON string representation of the object
print AuthorizationInfo.to_json()

# convert the object into a dict
authorization_info_dict = authorization_info_instance.to_dict()
# create an instance of AuthorizationInfo from a dict
authorization_info_form_dict = authorization_info.from_dict(authorization_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


