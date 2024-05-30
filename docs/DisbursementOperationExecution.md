# DisbursementOperationExecution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**DisbursementOperationInput**](DisbursementOperationInput.md) |  | 
**output** | [**DisbursementOperationExecutionOutput**](DisbursementOperationExecutionOutput.md) |  | [optional] 
**payout_id** | **str** |  | [optional] 
**started_at** | **float** |  | 
**finished_at** | **float** |  | [optional] 
**failure** | [**OperationExecutionFailure**](OperationExecutionFailure.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.disbursement_operation_execution import DisbursementOperationExecution

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementOperationExecution from a JSON string
disbursement_operation_execution_instance = DisbursementOperationExecution.from_json(json)
# print the JSON string representation of the object
print(DisbursementOperationExecution.to_json())

# convert the object into a dict
disbursement_operation_execution_dict = disbursement_operation_execution_instance.to_dict()
# create an instance of DisbursementOperationExecution from a dict
disbursement_operation_execution_from_dict = DisbursementOperationExecution.from_dict(disbursement_operation_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


