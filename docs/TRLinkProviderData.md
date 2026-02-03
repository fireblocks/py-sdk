# TRLinkProviderData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Provider name | [optional] 
**data** | **Dict[str, object]** | Provider-specific data | [optional] 

## Example

```python
from fireblocks.models.tr_link_provider_data import TRLinkProviderData

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkProviderData from a JSON string
tr_link_provider_data_instance = TRLinkProviderData.from_json(json)
# print the JSON string representation of the object
print(TRLinkProviderData.to_json())

# convert the object into a dict
tr_link_provider_data_dict = tr_link_provider_data_instance.to_dict()
# create an instance of TRLinkProviderData from a dict
tr_link_provider_data_from_dict = TRLinkProviderData.from_dict(tr_link_provider_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


