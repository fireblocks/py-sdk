# SwapFlowError

The error message for the swap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code representing the error | 
**message** | **str** | Error message | 

## Example

```python
from fireblocks.models.swap_flow_error import SwapFlowError

# TODO update the JSON string below
json = "{}"
# create an instance of SwapFlowError from a JSON string
swap_flow_error_instance = SwapFlowError.from_json(json)
# print the JSON string representation of the object
print(SwapFlowError.to_json())

# convert the object into a dict
swap_flow_error_dict = swap_flow_error_instance.to_dict()
# create an instance of SwapFlowError from a dict
swap_flow_error_from_dict = SwapFlowError.from_dict(swap_flow_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


