# Fee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | **str** | The type of fee, such as ORDER, NETWORK, or SPREAD. ORDER - Fee for executing the order. NETWORK - Fee for network transactions. SPREAD - Fee for the difference between buy and sell prices.  | 
**asset_id** | **str** | The asset identifier for the fee. | 
**amount_type** | **str** |  | 
**amount** | **float** | Fee in basis points (1 &#x3D; 0.01%, 10000 &#x3D; 100%) | 

## Example

```python
from fireblocks.models.fee import Fee

# TODO update the JSON string below
json = "{}"
# create an instance of Fee from a JSON string
fee_instance = Fee.from_json(json)
# print the JSON string representation of the object
print(Fee.to_json())

# convert the object into a dict
fee_dict = fee_instance.to_dict()
# create an instance of Fee from a dict
fee_from_dict = Fee.from_dict(fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


