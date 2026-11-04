# CosignerApiUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the API user | 
**last_seen** | **datetime** | The date the API user was last seen | [optional] 
**callback_handler** | [**CallbackHandler**](CallbackHandler.md) |  | [optional] 

## Example

```python
from fireblocks.models.cosigner_api_user import CosignerApiUser

# TODO update the JSON string below
json = "{}"
# create an instance of CosignerApiUser from a JSON string
cosigner_api_user_instance = CosignerApiUser.from_json(json)
# print the JSON string representation of the object
print(CosignerApiUser.to_json())

# convert the object into a dict
cosigner_api_user_dict = cosigner_api_user_instance.to_dict()
# create an instance of CosignerApiUser from a dict
cosigner_api_user_from_dict = CosignerApiUser.from_dict(cosigner_api_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


