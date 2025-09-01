# AmountRange

Amount range configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **str** | Minimum amount | 
**max** | **str** | Maximum amount | 
**currency** | **str** | Currency for the amount | 

## Example

```python
from fireblocks.models.amount_range import AmountRange

# TODO update the JSON string below
json = "{}"
# create an instance of AmountRange from a JSON string
amount_range_instance = AmountRange.from_json(json)
# print the JSON string representation of the object
print(AmountRange.to_json())

# convert the object into a dict
amount_range_dict = amount_range_instance.to_dict()
# create an instance of AmountRange from a dict
amount_range_from_dict = AmountRange.from_dict(amount_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


