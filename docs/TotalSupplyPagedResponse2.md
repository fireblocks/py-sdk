# TotalSupplyPagedResponse2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TotalSupplyItemDto]**](TotalSupplyItemDto.md) | Array of total supply data points | 
**next** | **str** | Cursor for next page | [optional] 
**prev** | **str** | Cursor for previous page | [optional] 
**total** | **float** | Total count of items | [optional] 

## Example

```python
from fireblocks.models.total_supply_paged_response2 import TotalSupplyPagedResponse2

# TODO update the JSON string below
json = "{}"
# create an instance of TotalSupplyPagedResponse2 from a JSON string
total_supply_paged_response2_instance = TotalSupplyPagedResponse2.from_json(json)
# print the JSON string representation of the object
print(TotalSupplyPagedResponse2.to_json())

# convert the object into a dict
total_supply_paged_response2_dict = total_supply_paged_response2_instance.to_dict()
# create an instance of TotalSupplyPagedResponse2 from a dict
total_supply_paged_response2_from_dict = TotalSupplyPagedResponse2.from_dict(total_supply_paged_response2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


