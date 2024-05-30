# PayoutInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**payee_account** | [**PayeeAccount**](PayeeAccount.md) |  | 
**amount** | [**InstructionAmount**](InstructionAmount.md) |  | 

## Example

```python
from fireblocks.models.payout_instruction import PayoutInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutInstruction from a JSON string
payout_instruction_instance = PayoutInstruction.from_json(json)
# print the JSON string representation of the object
print(PayoutInstruction.to_json())

# convert the object into a dict
payout_instruction_dict = payout_instruction_instance.to_dict()
# create an instance of PayoutInstruction from a dict
payout_instruction_from_dict = PayoutInstruction.from_dict(payout_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


