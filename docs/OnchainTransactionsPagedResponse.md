# OnchainTransactionsPagedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OnchainTransaction]**](OnchainTransaction.md) | Array of onchain transactions | 
**next** | **str** | Cursor for next page | [optional] 
**prev** | **str** | Cursor for previous page | [optional] 
**total** | **float** | Total count of items | [optional] 

## Example

```python
from fireblocks.models.onchain_transactions_paged_response import OnchainTransactionsPagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainTransactionsPagedResponse from a JSON string
onchain_transactions_paged_response_instance = OnchainTransactionsPagedResponse.from_json(json)
# print the JSON string representation of the object
print(OnchainTransactionsPagedResponse.to_json())

# convert the object into a dict
onchain_transactions_paged_response_dict = onchain_transactions_paged_response_instance.to_dict()
# create an instance of OnchainTransactionsPagedResponse from a dict
onchain_transactions_paged_response_from_dict = OnchainTransactionsPagedResponse.from_dict(onchain_transactions_paged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


