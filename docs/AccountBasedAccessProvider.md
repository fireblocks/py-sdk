# AccountBasedAccessProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the provider | 
**name** | **str** | Display name of the provider | 
**logo** | **str** | URL to the logo image of the provider | [optional] 
**account_based** | **bool** | Indicates whether the provider access model is through accounts or directly | 
**manifest** | [**Manifest**](Manifest.md) |  | 
**connected** | **bool** | Whether the provider is currently connected | 
**accounts** | [**List[AccountBase]**](AccountBase.md) |  | [optional] 

## Example

```python
from fireblocks.models.account_based_access_provider import AccountBasedAccessProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBasedAccessProvider from a JSON string
account_based_access_provider_instance = AccountBasedAccessProvider.from_json(json)
# print the JSON string representation of the object
print(AccountBasedAccessProvider.to_json())

# convert the object into a dict
account_based_access_provider_dict = account_based_access_provider_instance.to_dict()
# create an instance of AccountBasedAccessProvider from a dict
account_based_access_provider_from_dict = AccountBasedAccessProvider.from_dict(account_based_access_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


