# DisbursementOperationExecutionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruction_set** | [**List[DisbursementInstructionOutput]**](DisbursementInstructionOutput.md) |  | 

## Example

```python
from fireblocks_client.models.disbursement_operation_execution_output import DisbursementOperationExecutionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementOperationExecutionOutput from a JSON string
disbursement_operation_execution_output_instance = DisbursementOperationExecutionOutput.from_json(json)
# print the JSON string representation of the object
print DisbursementOperationExecutionOutput.to_json()

# convert the object into a dict
disbursement_operation_execution_output_dict = disbursement_operation_execution_output_instance.to_dict()
# create an instance of DisbursementOperationExecutionOutput from a dict
disbursement_operation_execution_output_form_dict = disbursement_operation_execution_output.from_dict(disbursement_operation_execution_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


