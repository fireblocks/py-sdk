# SwapOperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_quote_id** | **str** | An identifier that uniquely identifies the received quote | 
**fee_level** | **str** | The fee level of the transaction | [optional] 
**tx_note** | **str** | user note on the transaction | [optional] 

## Example

```python
from fireblocks.models.swap_operation_request import SwapOperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SwapOperationRequest from a JSON string
swap_operation_request_instance = SwapOperationRequest.from_json(json)
# print the JSON string representation of the object
print(SwapOperationRequest.to_json())

# convert the object into a dict
swap_operation_request_dict = swap_operation_request_instance.to_dict()
# create an instance of SwapOperationRequest from a dict
swap_operation_request_from_dict = SwapOperationRequest.from_dict(swap_operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


