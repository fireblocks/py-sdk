# ConfigOperationSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**type** | [**DisbursementOperationType**](DisbursementOperationType.md) |  | 
**params** | [**DisbursementOperationConfigParams**](DisbursementOperationConfigParams.md) |  | 

## Example

```python
from fireblocks.models.config_operation_snapshot import ConfigOperationSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigOperationSnapshot from a JSON string
config_operation_snapshot_instance = ConfigOperationSnapshot.from_json(json)
# print the JSON string representation of the object
print(ConfigOperationSnapshot.to_json())

# convert the object into a dict
config_operation_snapshot_dict = config_operation_snapshot_instance.to_dict()
# create an instance of ConfigOperationSnapshot from a dict
config_operation_snapshot_from_dict = ConfigOperationSnapshot.from_dict(config_operation_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


