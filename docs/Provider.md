# Provider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the provider | 
**provider_name** | **str** | Name of the provider | 
**validators** | [**List[Validator]**](Validator.md) | An array of objects that includes chain descriptors and the corresponding fee percentages for validators supported by the provider | 
**icon_url** | **str** | URL to the validator&#39;s icon | [optional] 
**terms_of_service_url** | **str** | URL to the terms of service | [optional] 
**is_terms_of_service_approved** | **bool** | Indicates whether the terms of service are approved | 
**is_private** | **bool** | Is the provider private, i.e created by the user | [optional] 
**is_liquid_staking** | **bool** | Is the provider a liquid staking provider | 

## Example

```python
from fireblocks.models.provider import Provider

# TODO update the JSON string below
json = "{}"
# create an instance of Provider from a JSON string
provider_instance = Provider.from_json(json)
# print the JSON string representation of the object
print(Provider.to_json())

# convert the object into a dict
provider_dict = provider_instance.to_dict()
# create an instance of Provider from a dict
provider_from_dict = Provider.from_dict(provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


