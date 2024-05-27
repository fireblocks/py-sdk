# ExchangeAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**ExchangeType**](ExchangeType.md) |  | [optional] 
**name** | **str** | Display name of the exchange account | [optional] 
**status** | **str** |  | [optional] 
**assets** | [**List[ExchangeAsset]**](ExchangeAsset.md) |  | [optional] 
**success** | **bool** | Did succeed in retrieve balance data | [optional] 
**trading_accounts** | [**List[ExchangeTradingAccount]**](ExchangeTradingAccount.md) |  | [optional] 
**is_subaccount** | **bool** | True if the account is a subaccount in an exchange | [optional] 
**main_account_id** | **str** | if the account is a sub-account, the ID of the main account | [optional] 

## Example

```python
from fireblocks_client.models.exchange_account import ExchangeAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeAccount from a JSON string
exchange_account_instance = ExchangeAccount.from_json(json)
# print the JSON string representation of the object
print ExchangeAccount.to_json()

# convert the object into a dict
exchange_account_dict = exchange_account_instance.to_dict()
# create an instance of ExchangeAccount from a dict
exchange_account_form_dict = exchange_account.from_dict(exchange_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


