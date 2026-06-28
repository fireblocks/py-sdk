# UtxoInputSelection

Explicitly control which UTXOs to include or exclude. This feature is currently in beta and might be subject to changes. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs_to_spend** | [**List[UtxoInput]**](UtxoInput.md) | Force-include specific UTXOs by txHash and index. | [optional] 
**inputs_to_exclude** | [**List[UtxoInput]**](UtxoInput.md) | Exclude specific UTXOs from selection. | [optional] 
**fill_fee_for_selected_inputs** | **bool** | When true and inputsToSpend is provided, automatically add more UTXOs to cover the transaction fee. Requires inputsToSpend.  | [optional] 

## Example

```python
from fireblocks.models.utxo_input_selection import UtxoInputSelection

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoInputSelection from a JSON string
utxo_input_selection_instance = UtxoInputSelection.from_json(json)
# print the JSON string representation of the object
print(UtxoInputSelection.to_json())

# convert the object into a dict
utxo_input_selection_dict = utxo_input_selection_instance.to_dict()
# create an instance of UtxoInputSelection from a dict
utxo_input_selection_from_dict = UtxoInputSelection.from_dict(utxo_input_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


