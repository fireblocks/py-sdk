# EarnProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | Stable protocol identifier (&#x60;MORPHO&#x60; or &#x60;AAVE&#x60;). | [optional] 
**display_name** | **str** | Human-readable protocol name for UI. | [optional] 
**logo_url** | **str** | URL for the provider logo asset. | [optional] 
**supported_chain_ids** | **List[int]** | EVM chain IDs where this provider is supported. | [optional] 
**is_terms_approval_required** | **bool** | Whether the user must accept terms before using this provider. | [optional] 
**terms_of_service_url** | **str** | URL to the provider terms of service, when applicable. | [optional] 
**is_terms_of_service_approved** | **bool** | Whether terms have been approved for this workspace / context. | [optional] 

## Example

```python
from fireblocks.models.earn_provider import EarnProvider

# TODO update the JSON string below
json = "{}"
# create an instance of EarnProvider from a JSON string
earn_provider_instance = EarnProvider.from_json(json)
# print the JSON string representation of the object
print(EarnProvider.to_json())

# convert the object into a dict
earn_provider_dict = earn_provider_instance.to_dict()
# create an instance of EarnProvider from a dict
earn_provider_from_dict = EarnProvider.from_dict(earn_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


