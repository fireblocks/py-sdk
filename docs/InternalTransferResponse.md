# InternalTransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates whether the transfer was successful | 

## Example

```python
from fireblocks.models.internal_transfer_response import InternalTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransferResponse from a JSON string
internal_transfer_response_instance = InternalTransferResponse.from_json(json)
# print the JSON string representation of the object
print(InternalTransferResponse.to_json())

# convert the object into a dict
internal_transfer_response_dict = internal_transfer_response_instance.to_dict()
# create an instance of InternalTransferResponse from a dict
internal_transfer_response_from_dict = InternalTransferResponse.from_dict(internal_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


