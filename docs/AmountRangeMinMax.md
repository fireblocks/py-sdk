# AmountRangeMinMax

Amount range with minimum and maximum values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **str** | Minimum amount | [optional] 
**max** | **str** | Maximum amount | [optional] 

## Example

```python
from fireblocks.models.amount_range_min_max import AmountRangeMinMax

# TODO update the JSON string below
json = "{}"
# create an instance of AmountRangeMinMax from a JSON string
amount_range_min_max_instance = AmountRangeMinMax.from_json(json)
# print the JSON string representation of the object
print(AmountRangeMinMax.to_json())

# convert the object into a dict
amount_range_min_max_dict = amount_range_min_max_instance.to_dict()
# create an instance of AmountRangeMinMax from a dict
amount_range_min_max_from_dict = AmountRangeMinMax.from_dict(amount_range_min_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


