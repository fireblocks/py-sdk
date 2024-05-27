# ExchangeAccountsPaged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_account** | [**List[ExchangeAccount]**](ExchangeAccount.md) |  | [optional] 
**paging** | [**ExchangeAccountsPagedPaging**](ExchangeAccountsPagedPaging.md) |  | [optional] 
**prev_url** | **str** |  | [optional] 
**next_url** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.exchange_accounts_paged import ExchangeAccountsPaged

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeAccountsPaged from a JSON string
exchange_accounts_paged_instance = ExchangeAccountsPaged.from_json(json)
# print the JSON string representation of the object
print ExchangeAccountsPaged.to_json()

# convert the object into a dict
exchange_accounts_paged_dict = exchange_accounts_paged_instance.to_dict()
# create an instance of ExchangeAccountsPaged from a dict
exchange_accounts_paged_form_dict = exchange_accounts_paged.from_dict(exchange_accounts_paged_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


