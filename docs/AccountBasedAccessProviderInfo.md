# AccountBasedAccessProviderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | **bool** | Whether the provider is currently connected | 
**accounts** | [**List[AccountBase]**](AccountBase.md) |  | 

## Example

```python
from fireblocks.models.account_based_access_provider_info import AccountBasedAccessProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBasedAccessProviderInfo from a JSON string
account_based_access_provider_info_instance = AccountBasedAccessProviderInfo.from_json(json)
# print the JSON string representation of the object
print(AccountBasedAccessProviderInfo.to_json())

# convert the object into a dict
account_based_access_provider_info_dict = account_based_access_provider_info_instance.to_dict()
# create an instance of AccountBasedAccessProviderInfo from a dict
account_based_access_provider_info_from_dict = AccountBasedAccessProviderInfo.from_dict(account_based_access_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


