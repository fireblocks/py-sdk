# ProviderID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The ID of the provider associated with the account. | 

## Example

```python
from fireblocks.models.provider_id import ProviderID

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderID from a JSON string
provider_id_instance = ProviderID.from_json(json)
# print the JSON string representation of the object
print(ProviderID.to_json())

# convert the object into a dict
provider_id_dict = provider_id_instance.to_dict()
# create an instance of ProviderID from a dict
provider_id_from_dict = ProviderID.from_dict(provider_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


