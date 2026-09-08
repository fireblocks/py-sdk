# CantonCallAllocationWithdraw


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Which call to make. Selects the shape of &#x60;payload&#x60;. | 
**payload** | [**AllocationWithdrawPayload**](AllocationWithdrawPayload.md) |  | 

## Example

```python
from fireblocks.models.canton_call_allocation_withdraw import CantonCallAllocationWithdraw

# TODO update the JSON string below
json = "{}"
# create an instance of CantonCallAllocationWithdraw from a JSON string
canton_call_allocation_withdraw_instance = CantonCallAllocationWithdraw.from_json(json)
# print the JSON string representation of the object
print(CantonCallAllocationWithdraw.to_json())

# convert the object into a dict
canton_call_allocation_withdraw_dict = canton_call_allocation_withdraw_instance.to_dict()
# create an instance of CantonCallAllocationWithdraw from a dict
canton_call_allocation_withdraw_from_dict = CantonCallAllocationWithdraw.from_dict(canton_call_allocation_withdraw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


