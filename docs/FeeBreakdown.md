# FeeBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **str** | Base fee component | [optional] 
**priority_fee** | **str** | Priority fee component | [optional] 
**rent** | **str** | Rent fee for Solana account creation/storage | [optional] 
**total_fee** | **str** | Total fee amount | [optional] 

## Example

```python
from fireblocks.models.fee_breakdown import FeeBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of FeeBreakdown from a JSON string
fee_breakdown_instance = FeeBreakdown.from_json(json)
# print the JSON string representation of the object
print(FeeBreakdown.to_json())

# convert the object into a dict
fee_breakdown_dict = fee_breakdown_instance.to_dict()
# create an instance of FeeBreakdown from a dict
fee_breakdown_from_dict = FeeBreakdown.from_dict(fee_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


