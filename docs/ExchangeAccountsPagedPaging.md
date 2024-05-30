# ExchangeAccountsPagedPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** | Query value to the after page | [optional] 
**before** | **str** | Query value to the before page | [optional] 

## Example

```python
from fireblocks_client.models.exchange_accounts_paged_paging import ExchangeAccountsPagedPaging

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeAccountsPagedPaging from a JSON string
exchange_accounts_paged_paging_instance = ExchangeAccountsPagedPaging.from_json(json)
# print the JSON string representation of the object
print(ExchangeAccountsPagedPaging.to_json())

# convert the object into a dict
exchange_accounts_paged_paging_dict = exchange_accounts_paged_paging_instance.to_dict()
# create an instance of ExchangeAccountsPagedPaging from a dict
exchange_accounts_paged_paging_from_dict = ExchangeAccountsPagedPaging.from_dict(exchange_accounts_paged_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


