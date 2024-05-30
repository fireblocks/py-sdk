# CreateTransferConfigOperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TransferOperationType**](TransferOperationType.md) |  | 
**params** | [**TransferOperationConfigParams**](TransferOperationConfigParams.md) |  | 

## Example

```python
from fireblocks_client.models.create_transfer_config_operation_request import CreateTransferConfigOperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransferConfigOperationRequest from a JSON string
create_transfer_config_operation_request_instance = CreateTransferConfigOperationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTransferConfigOperationRequest.to_json())

# convert the object into a dict
create_transfer_config_operation_request_dict = create_transfer_config_operation_request_instance.to_dict()
# create an instance of CreateTransferConfigOperationRequest from a dict
create_transfer_config_operation_request_from_dict = CreateTransferConfigOperationRequest.from_dict(create_transfer_config_operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


