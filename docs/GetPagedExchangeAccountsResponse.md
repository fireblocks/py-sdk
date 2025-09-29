# GetPagedExchangeAccountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchanges** | [**List[ExchangeAccount]**](ExchangeAccount.md) |  | 
**paging** | [**GetPagedExchangeAccountsResponsePaging**](GetPagedExchangeAccountsResponsePaging.md) |  | [optional] 
**prev_url** | **str** |  | [optional] 
**next_url** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.get_paged_exchange_accounts_response import GetPagedExchangeAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPagedExchangeAccountsResponse from a JSON string
get_paged_exchange_accounts_response_instance = GetPagedExchangeAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPagedExchangeAccountsResponse.to_json())

# convert the object into a dict
get_paged_exchange_accounts_response_dict = get_paged_exchange_accounts_response_instance.to_dict()
# create an instance of GetPagedExchangeAccountsResponse from a dict
get_paged_exchange_accounts_response_from_dict = GetPagedExchangeAccountsResponse.from_dict(get_paged_exchange_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


