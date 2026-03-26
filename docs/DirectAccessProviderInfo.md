# DirectAccessProviderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** | Whether the provider was approved for use | [optional] 
**has_terms_of_service** | **bool** | Whether the provider has terms of service | 
**terms_of_service_url** | **str** | URL to the terms of service document | [optional] 
**privacy_policy_url** | **str** | URL to the privacy policy document | [optional] 

## Example

```python
from fireblocks.models.direct_access_provider_info import DirectAccessProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DirectAccessProviderInfo from a JSON string
direct_access_provider_info_instance = DirectAccessProviderInfo.from_json(json)
# print the JSON string representation of the object
print(DirectAccessProviderInfo.to_json())

# convert the object into a dict
direct_access_provider_info_dict = direct_access_provider_info_instance.to_dict()
# create an instance of DirectAccessProviderInfo from a dict
direct_access_provider_info_from_dict = DirectAccessProviderInfo.from_dict(direct_access_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


