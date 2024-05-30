# DisbursementPercentageInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_account** | [**Destination**](Destination.md) |  | 
**asset_id** | **str** |  | 
**percentage** | **str** |  | 

## Example

```python
from fireblocks.models.disbursement_percentage_instruction import DisbursementPercentageInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementPercentageInstruction from a JSON string
disbursement_percentage_instruction_instance = DisbursementPercentageInstruction.from_json(json)
# print the JSON string representation of the object
print(DisbursementPercentageInstruction.to_json())

# convert the object into a dict
disbursement_percentage_instruction_dict = disbursement_percentage_instruction_instance.to_dict()
# create an instance of DisbursementPercentageInstruction from a dict
disbursement_percentage_instruction_from_dict = DisbursementPercentageInstruction.from_dict(disbursement_percentage_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


