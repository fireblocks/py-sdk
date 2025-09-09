# TradingProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the provider | 
**name** | **str** | Display name of the provider | 
**logo** | **str** | URL to the logo image of the provider | [optional] 
**account_based** | **bool** | Indicates whether the provider access model is through accounts or directly | 
**manifest** | [**Manifest**](Manifest.md) |  | 
**connected** | **bool** | Whether the provider is currently connected | 
**accounts** | [**List[AccountBase]**](AccountBase.md) |  | [optional] 
**approved** | **bool** | Whether the provider was approved for use | [optional] 
**has_terms_of_service** | **bool** | Whether the provider has terms of service | 
**terms_of_service_url** | **str** | URL to the terms of service document | [optional] 

## Example

```python
from fireblocks.models.trading_provider import TradingProvider

# TODO update the JSON string below
json = "{}"
# create an instance of TradingProvider from a JSON string
trading_provider_instance = TradingProvider.from_json(json)
# print the JSON string representation of the object
print(TradingProvider.to_json())

# convert the object into a dict
trading_provider_dict = trading_provider_instance.to_dict()
# create an instance of TradingProvider from a dict
trading_provider_from_dict = TradingProvider.from_dict(trading_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


