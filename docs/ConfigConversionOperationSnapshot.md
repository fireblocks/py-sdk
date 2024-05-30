# ConfigConversionOperationSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**type** | [**ConversionOperationType**](ConversionOperationType.md) |  | 
**params** | [**ConversionOperationConfigParams**](ConversionOperationConfigParams.md) |  | 

## Example

```python
from fireblocks_client.models.config_conversion_operation_snapshot import ConfigConversionOperationSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigConversionOperationSnapshot from a JSON string
config_conversion_operation_snapshot_instance = ConfigConversionOperationSnapshot.from_json(json)
# print the JSON string representation of the object
print(ConfigConversionOperationSnapshot.to_json())

# convert the object into a dict
config_conversion_operation_snapshot_dict = config_conversion_operation_snapshot_instance.to_dict()
# create an instance of ConfigConversionOperationSnapshot from a dict
config_conversion_operation_snapshot_from_dict = ConfigConversionOperationSnapshot.from_dict(config_conversion_operation_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


