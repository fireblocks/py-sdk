# BaseProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the provider | 
**name** | **str** | Display name of the provider | 
**logo** | **str** | URL to the logo image of the provider | [optional] 
**account_based** | **bool** | Indicates whether the provider access model is through accounts or directly | 

## Example

```python
from fireblocks.models.base_provider import BaseProvider

# TODO update the JSON string below
json = "{}"
# create an instance of BaseProvider from a JSON string
base_provider_instance = BaseProvider.from_json(json)
# print the JSON string representation of the object
print(BaseProvider.to_json())

# convert the object into a dict
base_provider_dict = base_provider_instance.to_dict()
# create an instance of BaseProvider from a dict
base_provider_from_dict = BaseProvider.from_dict(base_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


