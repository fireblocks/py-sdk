# CreateInternalTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | 
**amount** | **str** |  | 
**source_type** | [**TradingAccountType**](TradingAccountType.md) |  | 
**dest_type** | [**TradingAccountType**](TradingAccountType.md) |  | 

## Example

```python
from fireblocks.models.create_internal_transfer_request import CreateInternalTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInternalTransferRequest from a JSON string
create_internal_transfer_request_instance = CreateInternalTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInternalTransferRequest.to_json())

# convert the object into a dict
create_internal_transfer_request_dict = create_internal_transfer_request_instance.to_dict()
# create an instance of CreateInternalTransferRequest from a dict
create_internal_transfer_request_from_dict = CreateInternalTransferRequest.from_dict(create_internal_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


