# DisbursementAmountInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_account** | [**Destination**](Destination.md) |  | 
**asset_id** | **str** |  | 
**amount** | **str** |  | 

## Example

```python
from fireblocks.models.disbursement_amount_instruction import DisbursementAmountInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementAmountInstruction from a JSON string
disbursement_amount_instruction_instance = DisbursementAmountInstruction.from_json(json)
# print the JSON string representation of the object
print(DisbursementAmountInstruction.to_json())

# convert the object into a dict
disbursement_amount_instruction_dict = disbursement_amount_instruction_instance.to_dict()
# create an instance of DisbursementAmountInstruction from a dict
disbursement_amount_instruction_from_dict = DisbursementAmountInstruction.from_dict(disbursement_amount_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


