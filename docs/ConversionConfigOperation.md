# ConversionConfigOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**type** | [**ConversionOperationType**](ConversionOperationType.md) |  | 
**params** | [**ConversionOperationConfigParams**](ConversionOperationConfigParams.md) |  | 
**status** | [**ConfigOperationStatus**](ConfigOperationStatus.md) |  | 
**validation_failure** | [**ConversionValidationFailure**](ConversionValidationFailure.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.conversion_config_operation import ConversionConfigOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionConfigOperation from a JSON string
conversion_config_operation_instance = ConversionConfigOperation.from_json(json)
# print the JSON string representation of the object
print ConversionConfigOperation.to_json()

# convert the object into a dict
conversion_config_operation_dict = conversion_config_operation_instance.to_dict()
# create an instance of ConversionConfigOperation from a dict
conversion_config_operation_form_dict = conversion_config_operation.from_dict(conversion_config_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


