# TransferConfigOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**type** | [**TransferOperationType**](TransferOperationType.md) |  | 
**params** | [**TransferOperationConfigParams**](TransferOperationConfigParams.md) |  | 
**status** | [**ConfigOperationStatus**](ConfigOperationStatus.md) |  | 
**validation_failure** | [**TransferValidationFailure**](TransferValidationFailure.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.transfer_config_operation import TransferConfigOperation

# TODO update the JSON string below
json = "{}"
# create an instance of TransferConfigOperation from a JSON string
transfer_config_operation_instance = TransferConfigOperation.from_json(json)
# print the JSON string representation of the object
print(TransferConfigOperation.to_json())

# convert the object into a dict
transfer_config_operation_dict = transfer_config_operation_instance.to_dict()
# create an instance of TransferConfigOperation from a dict
transfer_config_operation_from_dict = TransferConfigOperation.from_dict(transfer_config_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


