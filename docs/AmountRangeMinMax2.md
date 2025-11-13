# AmountRangeMinMax2

Amount range with minimum and maximum values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **str** | Minimum amount | 
**max** | **str** | Maximum amount | [optional] 

## Example

```python
from fireblocks.models.amount_range_min_max2 import AmountRangeMinMax2

# TODO update the JSON string below
json = "{}"
# create an instance of AmountRangeMinMax2 from a JSON string
amount_range_min_max2_instance = AmountRangeMinMax2.from_json(json)
# print the JSON string representation of the object
print(AmountRangeMinMax2.to_json())

# convert the object into a dict
amount_range_min_max2_dict = amount_range_min_max2_instance.to_dict()
# create an instance of AmountRangeMinMax2 from a dict
amount_range_min_max2_from_dict = AmountRangeMinMax2.from_dict(amount_range_min_max2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


