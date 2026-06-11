# BalanceHistoryPagedResponse2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BalanceHistoryItemDto]**](BalanceHistoryItemDto.md) | Array of balance history data points | 
**next** | **str** | Cursor for next page | [optional] 
**prev** | **str** | Cursor for previous page | [optional] 
**total** | **float** | Total count of items | [optional] 

## Example

```python
from fireblocks.models.balance_history_paged_response2 import BalanceHistoryPagedResponse2

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistoryPagedResponse2 from a JSON string
balance_history_paged_response2_instance = BalanceHistoryPagedResponse2.from_json(json)
# print the JSON string representation of the object
print(BalanceHistoryPagedResponse2.to_json())

# convert the object into a dict
balance_history_paged_response2_dict = balance_history_paged_response2_instance.to_dict()
# create an instance of BalanceHistoryPagedResponse2 from a dict
balance_history_paged_response2_from_dict = BalanceHistoryPagedResponse2.from_dict(balance_history_paged_response2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


