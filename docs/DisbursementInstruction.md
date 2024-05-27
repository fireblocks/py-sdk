# DisbursementInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_account** | [**Destination**](Destination.md) |  | 
**asset_id** | **str** |  | 
**amount** | **str** |  | 
**percentage** | **str** |  | 

## Example

```python
from fireblocks_client.models.disbursement_instruction import DisbursementInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementInstruction from a JSON string
disbursement_instruction_instance = DisbursementInstruction.from_json(json)
# print the JSON string representation of the object
print DisbursementInstruction.to_json()

# convert the object into a dict
disbursement_instruction_dict = disbursement_instruction_instance.to_dict()
# create an instance of DisbursementInstruction from a dict
disbursement_instruction_form_dict = disbursement_instruction.from_dict(disbursement_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


