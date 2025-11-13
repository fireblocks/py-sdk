# DirectAccessProviderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** | Whether the provider was approved for use | [optional] 
**has_terms_of_service** | **bool** | Whether the provider has terms of service | 
**terms_of_service_url** | **str** | URL to the terms of service document | [optional] 

## Example

```python
from fireblocks.models.direct_access_provider_details import DirectAccessProviderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DirectAccessProviderDetails from a JSON string
direct_access_provider_details_instance = DirectAccessProviderDetails.from_json(json)
# print the JSON string representation of the object
print(DirectAccessProviderDetails.to_json())

# convert the object into a dict
direct_access_provider_details_dict = direct_access_provider_details_instance.to_dict()
# create an instance of DirectAccessProviderDetails from a dict
direct_access_provider_details_from_dict = DirectAccessProviderDetails.from_dict(direct_access_provider_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


