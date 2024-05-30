# DisbursementInstructionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**AssetAmount**](AssetAmount.md) |  | 
**fee** | [**AssetAmount**](AssetAmount.md) |  | 
**payee_account** | [**Destination**](Destination.md) |  | 

## Example

```python
from fireblocks.models.disbursement_instruction_output import DisbursementInstructionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementInstructionOutput from a JSON string
disbursement_instruction_output_instance = DisbursementInstructionOutput.from_json(json)
# print the JSON string representation of the object
print(DisbursementInstructionOutput.to_json())

# convert the object into a dict
disbursement_instruction_output_dict = disbursement_instruction_output_instance.to_dict()
# create an instance of DisbursementInstructionOutput from a dict
disbursement_instruction_output_from_dict = DisbursementInstructionOutput.from_dict(disbursement_instruction_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


