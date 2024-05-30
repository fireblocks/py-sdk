# ExchangeTradingAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**assets** | [**List[ExchangeAsset]**](ExchangeAsset.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.exchange_trading_account import ExchangeTradingAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeTradingAccount from a JSON string
exchange_trading_account_instance = ExchangeTradingAccount.from_json(json)
# print the JSON string representation of the object
print(ExchangeTradingAccount.to_json())

# convert the object into a dict
exchange_trading_account_dict = exchange_trading_account_instance.to_dict()
# create an instance of ExchangeTradingAccount from a dict
exchange_trading_account_from_dict = ExchangeTradingAccount.from_dict(exchange_trading_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


