# ConfigTransferOperationSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**type** | [**TransferOperationType**](TransferOperationType.md) |  | 
**params** | [**TransferOperationConfigParams**](TransferOperationConfigParams.md) |  | 

## Example

```python
from fireblocks.models.config_transfer_operation_snapshot import ConfigTransferOperationSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigTransferOperationSnapshot from a JSON string
config_transfer_operation_snapshot_instance = ConfigTransferOperationSnapshot.from_json(json)
# print the JSON string representation of the object
print(ConfigTransferOperationSnapshot.to_json())

# convert the object into a dict
config_transfer_operation_snapshot_dict = config_transfer_operation_snapshot_instance.to_dict()
# create an instance of ConfigTransferOperationSnapshot from a dict
config_transfer_operation_snapshot_from_dict = ConfigTransferOperationSnapshot.from_dict(config_transfer_operation_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


