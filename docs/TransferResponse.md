# TransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the transfer offer. | 

## Example

```python
from fireblocks.models.transfer_response import TransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferResponse from a JSON string
transfer_response_instance = TransferResponse.from_json(json)
# print the JSON string representation of the object
print(TransferResponse.to_json())

# convert the object into a dict
transfer_response_dict = transfer_response_instance.to_dict()
# create an instance of TransferResponse from a dict
transfer_response_from_dict = TransferResponse.from_dict(transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


