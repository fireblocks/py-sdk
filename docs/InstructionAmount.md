# InstructionAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | 
**asset_id** | **str** |  | 

## Example

```python
from fireblocks_client.models.instruction_amount import InstructionAmount

# TODO update the JSON string below
json = "{}"
# create an instance of InstructionAmount from a JSON string
instruction_amount_instance = InstructionAmount.from_json(json)
# print the JSON string representation of the object
print InstructionAmount.to_json()

# convert the object into a dict
instruction_amount_dict = instruction_amount_instance.to_dict()
# create an instance of InstructionAmount from a dict
instruction_amount_form_dict = instruction_amount.from_dict(instruction_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


