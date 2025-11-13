# TRLinkProviderResult

Provider-specific response data wrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_response** | **object** | Raw provider response | [optional] 

## Example

```python
from fireblocks.models.tr_link_provider_result import TRLinkProviderResult

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkProviderResult from a JSON string
tr_link_provider_result_instance = TRLinkProviderResult.from_json(json)
# print the JSON string representation of the object
print(TRLinkProviderResult.to_json())

# convert the object into a dict
tr_link_provider_result_dict = tr_link_provider_result_instance.to_dict()
# create an instance of TRLinkProviderResult from a dict
tr_link_provider_result_from_dict = TRLinkProviderResult.from_dict(tr_link_provider_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


