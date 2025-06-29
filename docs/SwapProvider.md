# SwapProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the provider | 
**name** | **str** | Name of the provider | 
**protocols** | [**List[SwapProviderProtocolsEnum]**](SwapProviderProtocolsEnum.md) | List of supported protocols. Protocols are specific per provider | 
**category** | [**ProviderCategoryEnum**](ProviderCategoryEnum.md) |  | 
**is_terms_approval_required** | **bool** | Indicates whether the terms of service are required for the provider. if &#x60;true&#x60;, the user must approve the terms of service before using the provider. otherwise, &#x60;termsOfServiceUrl&#x60; and &#x60;isTermsOfServiceApproved&#x60; are not shown under the provider data. | 
**terms_of_service_url** | **str** | URL to the terms of service | [optional] 
**is_terms_of_service_approved** | **bool** | Indicates whether the terms of service are approved by the user | [optional] 

## Example

```python
from fireblocks.models.swap_provider import SwapProvider

# TODO update the JSON string below
json = "{}"
# create an instance of SwapProvider from a JSON string
swap_provider_instance = SwapProvider.from_json(json)
# print the JSON string representation of the object
print(SwapProvider.to_json())

# convert the object into a dict
swap_provider_dict = swap_provider_instance.to_dict()
# create an instance of SwapProvider from a dict
swap_provider_from_dict = SwapProvider.from_dict(swap_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


