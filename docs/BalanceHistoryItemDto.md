# BalanceHistoryItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp of the data point | 
**balance** | **str** | Balance at the given timestamp | 

## Example

```python
from fireblocks.models.balance_history_item_dto import BalanceHistoryItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistoryItemDto from a JSON string
balance_history_item_dto_instance = BalanceHistoryItemDto.from_json(json)
# print the JSON string representation of the object
print(BalanceHistoryItemDto.to_json())

# convert the object into a dict
balance_history_item_dto_dict = balance_history_item_dto_instance.to_dict()
# create an instance of BalanceHistoryItemDto from a dict
balance_history_item_dto_from_dict = BalanceHistoryItemDto.from_dict(balance_history_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


