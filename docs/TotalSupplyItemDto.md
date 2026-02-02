# TotalSupplyItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp of the data point | 
**total_supply** | **str** | Total supply at the given timestamp | 

## Example

```python
from fireblocks.models.total_supply_item_dto import TotalSupplyItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of TotalSupplyItemDto from a JSON string
total_supply_item_dto_instance = TotalSupplyItemDto.from_json(json)
# print the JSON string representation of the object
print(TotalSupplyItemDto.to_json())

# convert the object into a dict
total_supply_item_dto_dict = total_supply_item_dto_instance.to_dict()
# create an instance of TotalSupplyItemDto from a dict
total_supply_item_dto_from_dict = TotalSupplyItemDto.from_dict(total_supply_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


