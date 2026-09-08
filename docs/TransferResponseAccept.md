# TransferResponseAccept

Accept an inbound 2-step transfer offer. Carries no arguments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the transfer offer. | 

## Example

```python
from fireblocks.models.transfer_response_accept import TransferResponseAccept

# TODO update the JSON string below
json = "{}"
# create an instance of TransferResponseAccept from a JSON string
transfer_response_accept_instance = TransferResponseAccept.from_json(json)
# print the JSON string representation of the object
print(TransferResponseAccept.to_json())

# convert the object into a dict
transfer_response_accept_dict = transfer_response_accept_instance.to_dict()
# create an instance of TransferResponseAccept from a dict
transfer_response_accept_from_dict = TransferResponseAccept.from_dict(transfer_response_accept_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


