# InternalTransferRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**source_type** | [**TradingAccountType**](TradingAccountType.md) |  | [optional] 
**dest_type** | [**TradingAccountType**](TradingAccountType.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.internal_transfer_request import InternalTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransferRequest from a JSON string
internal_transfer_request_instance = InternalTransferRequest.from_json(json)
# print the JSON string representation of the object
print InternalTransferRequest.to_json()

# convert the object into a dict
internal_transfer_request_dict = internal_transfer_request_instance.to_dict()
# create an instance of InternalTransferRequest from a dict
internal_transfer_request_form_dict = internal_transfer_request.from_dict(internal_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


