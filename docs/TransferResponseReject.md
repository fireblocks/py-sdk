# TransferResponseReject

Reject an inbound 2-step transfer offer. Carries no arguments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the transfer offer. | 

## Example

```python
from fireblocks.models.transfer_response_reject import TransferResponseReject

# TODO update the JSON string below
json = "{}"
# create an instance of TransferResponseReject from a JSON string
transfer_response_reject_instance = TransferResponseReject.from_json(json)
# print the JSON string representation of the object
print(TransferResponseReject.to_json())

# convert the object into a dict
transfer_response_reject_dict = transfer_response_reject_instance.to_dict()
# create an instance of TransferResponseReject from a dict
transfer_response_reject_from_dict = TransferResponseReject.from_dict(transfer_response_reject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


