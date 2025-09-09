# BpsFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_type** | **str** |  | 
**amount** | **float** | Fee in basis points (1 &#x3D; 0.01%, 10000 &#x3D; 100%) | 

## Example

```python
from fireblocks.models.bps_fee import BpsFee

# TODO update the JSON string below
json = "{}"
# create an instance of BpsFee from a JSON string
bps_fee_instance = BpsFee.from_json(json)
# print the JSON string representation of the object
print(BpsFee.to_json())

# convert the object into a dict
bps_fee_dict = bps_fee_instance.to_dict()
# create an instance of BpsFee from a dict
bps_fee_from_dict = BpsFee.from_dict(bps_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


