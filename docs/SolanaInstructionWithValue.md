# SolanaInstructionWithValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the instruction | 
**discriminator** | **List[float]** | The discriminator for the instruction. Acts as a function selector | 
**accounts** | [**List[SOLAccountWithValue]**](SOLAccountWithValue.md) |  | 
**args** | [**List[SolParameterWithValue]**](SolParameterWithValue.md) | The arguments of the instruction | 

## Example

```python
from fireblocks.models.solana_instruction_with_value import SolanaInstructionWithValue

# TODO update the JSON string below
json = "{}"
# create an instance of SolanaInstructionWithValue from a JSON string
solana_instruction_with_value_instance = SolanaInstructionWithValue.from_json(json)
# print the JSON string representation of the object
print(SolanaInstructionWithValue.to_json())

# convert the object into a dict
solana_instruction_with_value_dict = solana_instruction_with_value_instance.to_dict()
# create an instance of SolanaInstructionWithValue from a dict
solana_instruction_with_value_from_dict = SolanaInstructionWithValue.from_dict(solana_instruction_with_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


