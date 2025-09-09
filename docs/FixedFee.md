# FixedFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_type** | **str** |  | 
**amount** | **str** | The fixed amount of the fee | 

## Example

```python
from fireblocks.models.fixed_fee import FixedFee

# TODO update the JSON string below
json = "{}"
# create an instance of FixedFee from a JSON string
fixed_fee_instance = FixedFee.from_json(json)
# print the JSON string representation of the object
print(FixedFee.to_json())

# convert the object into a dict
fixed_fee_dict = fixed_fee_instance.to_dict()
# create an instance of FixedFee from a dict
fixed_fee_from_dict = FixedFee.from_dict(fixed_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


