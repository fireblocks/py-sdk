# TradingProviderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the provider | 
**name** | **str** | Display name of the provider | 
**logo** | **str** | URL to the logo image of the provider | [optional] 
**account_based** | **bool** | Indicates whether the provider access model is through accounts or directly | 
**manifest** | [**Manifest**](Manifest.md) |  | 
**connected** | **bool** | Whether the provider is currently connected | 
**accounts** | [**List[AccountBase]**](AccountBase.md) |  | 
**approved** | **bool** | Whether the provider was approved for use | [optional] 
**has_terms_of_service** | **bool** | Whether the provider has terms of service | 
**terms_of_service_url** | **str** | URL to the terms of service document | [optional] 
**privacy_policy_url** | **str** | URL to the privacy policy document | [optional] 

## Example

```python
from fireblocks.models.trading_provider_details import TradingProviderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TradingProviderDetails from a JSON string
trading_provider_details_instance = TradingProviderDetails.from_json(json)
# print the JSON string representation of the object
print(TradingProviderDetails.to_json())

# convert the object into a dict
trading_provider_details_dict = trading_provider_details_instance.to_dict()
# create an instance of TradingProviderDetails from a dict
trading_provider_details_from_dict = TradingProviderDetails.from_dict(trading_provider_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


