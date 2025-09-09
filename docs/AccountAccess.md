# AccountAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates this uses account-based access | 
**provider_id** | **str** | The ID of the provider | [optional] 
**account_id** | **str** | The ID of the account | 

## Example

```python
from fireblocks.models.account_access import AccountAccess

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAccess from a JSON string
account_access_instance = AccountAccess.from_json(json)
# print the JSON string representation of the object
print(AccountAccess.to_json())

# convert the object into a dict
account_access_dict = account_access_instance.to_dict()
# create an instance of AccountAccess from a dict
account_access_from_dict = AccountAccess.from_dict(account_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


