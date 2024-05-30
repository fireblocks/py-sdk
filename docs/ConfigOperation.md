# ConfigOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**type** | [**DisbursementOperationType**](DisbursementOperationType.md) |  | 
**params** | [**DisbursementOperationConfigParams**](DisbursementOperationConfigParams.md) |  | 
**status** | [**ConfigOperationStatus**](ConfigOperationStatus.md) |  | 
**validation_failure** | [**DisbursementValidationFailure**](DisbursementValidationFailure.md) |  | [optional] 

## Example

```python
from fireblocks.models.config_operation import ConfigOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigOperation from a JSON string
config_operation_instance = ConfigOperation.from_json(json)
# print the JSON string representation of the object
print(ConfigOperation.to_json())

# convert the object into a dict
config_operation_dict = config_operation_instance.to_dict()
# create an instance of ConfigOperation from a dict
config_operation_from_dict = ConfigOperation.from_dict(config_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


