# DirectAccessProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the provider | 
**name** | **str** | Display name of the provider | 
**logo** | **str** | URL to the logo image of the provider | [optional] 
**account_based** | **bool** | Indicates whether the provider access model is through accounts or directly | 
**approved** | **bool** | Whether the provider was approved for use | [optional] 
**has_terms_of_service** | **bool** | Whether the provider has terms of service | 
**terms_of_service_url** | **str** | URL to the terms of service document | [optional] 

## Example

```python
from fireblocks.models.direct_access_provider import DirectAccessProvider

# TODO update the JSON string below
json = "{}"
# create an instance of DirectAccessProvider from a JSON string
direct_access_provider_instance = DirectAccessProvider.from_json(json)
# print the JSON string representation of the object
print(DirectAccessProvider.to_json())

# convert the object into a dict
direct_access_provider_dict = direct_access_provider_instance.to_dict()
# create an instance of DirectAccessProvider from a dict
direct_access_provider_from_dict = DirectAccessProvider.from_dict(direct_access_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


