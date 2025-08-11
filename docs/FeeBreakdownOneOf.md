# FeeBreakdownOneOf

Solana-specific fee breakdown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **str** | Base fee for Solana transaction | [optional] 
**priority_fee** | **str** | Priority fee for Solana transaction | [optional] 
**rent** | **str** | Rent fee for Solana account creation/storage | [optional] 
**total_fee** | **str** | Total fee amount | [optional] 

## Example

```python
from fireblocks.models.fee_breakdown_one_of import FeeBreakdownOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of FeeBreakdownOneOf from a JSON string
fee_breakdown_one_of_instance = FeeBreakdownOneOf.from_json(json)
# print the JSON string representation of the object
print(FeeBreakdownOneOf.to_json())

# convert the object into a dict
fee_breakdown_one_of_dict = fee_breakdown_one_of_instance.to_dict()
# create an instance of FeeBreakdownOneOf from a dict
fee_breakdown_one_of_from_dict = FeeBreakdownOneOf.from_dict(fee_breakdown_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


