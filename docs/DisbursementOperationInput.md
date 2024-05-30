# DisbursementOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**payment_account** | [**Account**](Account.md) |  | 
**instruction_set** | [**List[DisbursementInstruction]**](DisbursementInstruction.md) |  | 

## Example

```python
from fireblocks.models.disbursement_operation_input import DisbursementOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementOperationInput from a JSON string
disbursement_operation_input_instance = DisbursementOperationInput.from_json(json)
# print the JSON string representation of the object
print(DisbursementOperationInput.to_json())

# convert the object into a dict
disbursement_operation_input_dict = disbursement_operation_input_instance.to_dict()
# create an instance of DisbursementOperationInput from a dict
disbursement_operation_input_from_dict = DisbursementOperationInput.from_dict(disbursement_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


