# AccountBasedAccessProviderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest** | [**Manifest**](Manifest.md) |  | 
**connected** | **bool** | Whether the provider is currently connected | 
**accounts** | [**List[AccountBase]**](AccountBase.md) |  | [optional] 

## Example

```python
from fireblocks.models.account_based_access_provider_details import AccountBasedAccessProviderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBasedAccessProviderDetails from a JSON string
account_based_access_provider_details_instance = AccountBasedAccessProviderDetails.from_json(json)
# print the JSON string representation of the object
print(AccountBasedAccessProviderDetails.to_json())

# convert the object into a dict
account_based_access_provider_details_dict = account_based_access_provider_details_instance.to_dict()
# create an instance of AccountBasedAccessProviderDetails from a dict
account_based_access_provider_details_from_dict = AccountBasedAccessProviderDetails.from_dict(account_based_access_provider_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


