# DisbursementConfigOperation


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
from fireblocks_client.models.disbursement_config_operation import DisbursementConfigOperation

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementConfigOperation from a JSON string
disbursement_config_operation_instance = DisbursementConfigOperation.from_json(json)
# print the JSON string representation of the object
print DisbursementConfigOperation.to_json()

# convert the object into a dict
disbursement_config_operation_dict = disbursement_config_operation_instance.to_dict()
# create an instance of DisbursementConfigOperation from a dict
disbursement_config_operation_form_dict = disbursement_config_operation.from_dict(disbursement_config_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


