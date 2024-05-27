# PayoutInstructionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**payee_account** | [**PayeeAccountResponse**](PayeeAccountResponse.md) |  | 
**amount** | [**InstructionAmount**](InstructionAmount.md) |  | 
**state** | [**PayoutInstructionState**](PayoutInstructionState.md) |  | 
**transactions** | [**List[Transaction]**](Transaction.md) |  | 

## Example

```python
from fireblocks_client.models.payout_instruction_response import PayoutInstructionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutInstructionResponse from a JSON string
payout_instruction_response_instance = PayoutInstructionResponse.from_json(json)
# print the JSON string representation of the object
print PayoutInstructionResponse.to_json()

# convert the object into a dict
payout_instruction_response_dict = payout_instruction_response_instance.to_dict()
# create an instance of PayoutInstructionResponse from a dict
payout_instruction_response_form_dict = payout_instruction_response.from_dict(payout_instruction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


