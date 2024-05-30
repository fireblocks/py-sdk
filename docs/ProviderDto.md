# ProviderDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the provider | 
**provider_name** | **str** | Name of the provider | 
**validators** | [**List[ValidatorDto]**](ValidatorDto.md) | An array of objects that includes chain descriptors and the corresponding fee percentages for validators supported by the provider | 
**icon_url** | **str** | URL to the validator&#39;s icon | 
**terms_of_service_url** | **str** | URL to the terms of service | 
**is_terms_of_service_approved** | **bool** | Indicates whether the terms of service are approved | 

## Example

```python
from fireblocks_client.models.provider_dto import ProviderDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderDto from a JSON string
provider_dto_instance = ProviderDto.from_json(json)
# print the JSON string representation of the object
print(ProviderDto.to_json())

# convert the object into a dict
provider_dto_dict = provider_dto_instance.to_dict()
# create an instance of ProviderDto from a dict
provider_dto_from_dict = ProviderDto.from_dict(provider_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


