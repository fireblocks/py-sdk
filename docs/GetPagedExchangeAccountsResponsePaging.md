# GetPagedExchangeAccountsResponsePaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** | Query value to the after page | [optional] 
**before** | **str** | Query value to the before page | [optional] 

## Example

```python
from fireblocks.models.get_paged_exchange_accounts_response_paging import GetPagedExchangeAccountsResponsePaging

# TODO update the JSON string below
json = "{}"
# create an instance of GetPagedExchangeAccountsResponsePaging from a JSON string
get_paged_exchange_accounts_response_paging_instance = GetPagedExchangeAccountsResponsePaging.from_json(json)
# print the JSON string representation of the object
print(GetPagedExchangeAccountsResponsePaging.to_json())

# convert the object into a dict
get_paged_exchange_accounts_response_paging_dict = get_paged_exchange_accounts_response_paging_instance.to_dict()
# create an instance of GetPagedExchangeAccountsResponsePaging from a dict
get_paged_exchange_accounts_response_paging_from_dict = GetPagedExchangeAccountsResponsePaging.from_dict(get_paged_exchange_accounts_response_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


