# SolanaInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the instruction | 
**discriminator** | **List[float]** | The discriminator for the instruction. Acts as a function selector | 
**accounts** | [**List[SOLAccount]**](SOLAccount.md) |  | 
**args** | [**List[SolParameter]**](SolParameter.md) |  | 

## Example

```python
from fireblocks.models.solana_instruction import SolanaInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of SolanaInstruction from a JSON string
solana_instruction_instance = SolanaInstruction.from_json(json)
# print the JSON string representation of the object
print(SolanaInstruction.to_json())

# convert the object into a dict
solana_instruction_dict = solana_instruction_instance.to_dict()
# create an instance of SolanaInstruction from a dict
solana_instruction_from_dict = SolanaInstruction.from_dict(solana_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


