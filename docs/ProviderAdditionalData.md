# ProviderAdditionalData

Provider specific additional data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_impact** | **str** |  | 

## Example

```python
from fireblocks.models.provider_additional_data import ProviderAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderAdditionalData from a JSON string
provider_additional_data_instance = ProviderAdditionalData.from_json(json)
# print the JSON string representation of the object
print(ProviderAdditionalData.to_json())

# convert the object into a dict
provider_additional_data_dict = provider_additional_data_instance.to_dict()
# create an instance of ProviderAdditionalData from a dict
provider_additional_data_from_dict = ProviderAdditionalData.from_dict(provider_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


