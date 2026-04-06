# AccountBasedProviderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the provider | 
**name** | **str** | Display name of the provider | 
**logo** | **str** | URL to the logo image of the provider | [optional] 
**account_based** | **bool** | Indicates whether the provider access model is through accounts or directly | 
**manifest** | [**Manifest**](Manifest.md) |  | 
**connected** | **bool** | Whether the provider is currently connected | 
**accounts** | [**List[AccountBase]**](AccountBase.md) |  | 

## Example

```python
from fireblocks.models.account_based_provider_details import AccountBasedProviderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBasedProviderDetails from a JSON string
account_based_provider_details_instance = AccountBasedProviderDetails.from_json(json)
# print the JSON string representation of the object
print(AccountBasedProviderDetails.to_json())

# convert the object into a dict
account_based_provider_details_dict = account_based_provider_details_instance.to_dict()
# create an instance of AccountBasedProviderDetails from a dict
account_based_provider_details_from_dict = AccountBasedProviderDetails.from_dict(account_based_provider_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


