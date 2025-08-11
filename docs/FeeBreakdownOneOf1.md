# FeeBreakdownOneOf1

Generic fee breakdown for other blockchains

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **str** | Base fee component | [optional] 
**priority_fee** | **str** | Priority fee component | [optional] 
**total_fee** | **str** | Total fee amount | [optional] 

## Example

```python
from fireblocks.models.fee_breakdown_one_of1 import FeeBreakdownOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of FeeBreakdownOneOf1 from a JSON string
fee_breakdown_one_of1_instance = FeeBreakdownOneOf1.from_json(json)
# print the JSON string representation of the object
print(FeeBreakdownOneOf1.to_json())

# convert the object into a dict
fee_breakdown_one_of1_dict = fee_breakdown_one_of1_instance.to_dict()
# create an instance of FeeBreakdownOneOf1 from a dict
fee_breakdown_one_of1_from_dict = FeeBreakdownOneOf1.from_dict(fee_breakdown_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


