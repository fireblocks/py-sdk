# SwapRequiredAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SwapRequiredActionsEnum**](SwapRequiredActionsEnum.md) |  | 
**status** | **str** | The status of the required action | 
**tx_id** | **str** | The transaction id of the required action | [optional] 

## Example

```python
from fireblocks.models.swap_required_action import SwapRequiredAction

# TODO update the JSON string below
json = "{}"
# create an instance of SwapRequiredAction from a JSON string
swap_required_action_instance = SwapRequiredAction.from_json(json)
# print the JSON string representation of the object
print(SwapRequiredAction.to_json())

# convert the object into a dict
swap_required_action_dict = swap_required_action_instance.to_dict()
# create an instance of SwapRequiredAction from a dict
swap_required_action_from_dict = SwapRequiredAction.from_dict(swap_required_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


