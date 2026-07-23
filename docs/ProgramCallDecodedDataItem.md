# ProgramCallDecodedDataItem

A single decoded Solana instruction from a PROGRAM_CALL transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **str** | The on-chain program address that owns this instruction. | 
**program_name** | **str** | Human-readable program name (e.g. &#x60;SystemProgram&#x60;, &#x60;ComputeBudget&#x60;). | 
**instruction_data** | **Dict[str, object]** | Decoded instruction arguments. Keys and values depend on the instruction type — values may be strings, numbers, or nested objects (e.g. &#x60;args&#x60;, &#x60;accounts&#x60;, &#x60;name&#x60;). | 

## Example

```python
from fireblocks.models.program_call_decoded_data_item import ProgramCallDecodedDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramCallDecodedDataItem from a JSON string
program_call_decoded_data_item_instance = ProgramCallDecodedDataItem.from_json(json)
# print the JSON string representation of the object
print(ProgramCallDecodedDataItem.to_json())

# convert the object into a dict
program_call_decoded_data_item_dict = program_call_decoded_data_item_instance.to_dict()
# create an instance of ProgramCallDecodedDataItem from a dict
program_call_decoded_data_item_from_dict = ProgramCallDecodedDataItem.from_dict(program_call_decoded_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


