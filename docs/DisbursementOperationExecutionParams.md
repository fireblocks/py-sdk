# DisbursementOperationExecutionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_operation_id** | **str** |  | 
**execution_params** | [**DisbursementOperationExecutionParamsExecutionParams**](DisbursementOperationExecutionParamsExecutionParams.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.disbursement_operation_execution_params import DisbursementOperationExecutionParams

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementOperationExecutionParams from a JSON string
disbursement_operation_execution_params_instance = DisbursementOperationExecutionParams.from_json(json)
# print the JSON string representation of the object
print DisbursementOperationExecutionParams.to_json()

# convert the object into a dict
disbursement_operation_execution_params_dict = disbursement_operation_execution_params_instance.to_dict()
# create an instance of DisbursementOperationExecutionParams from a dict
disbursement_operation_execution_params_form_dict = disbursement_operation_execution_params.from_dict(disbursement_operation_execution_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


