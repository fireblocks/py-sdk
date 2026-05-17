# UtxoSelectionParams

For UTXO-based blockchains only. Controls which UTXOs are used for automatic selection. Cannot be used together with extraParameters.inputsSelection. This feature is currently in beta and might be subject to changes. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection_strategy** | **str** | Optional override for the UTXO selection strategy configured at the vault/tenant level.  | [optional] 
**filters** | [**UtxoSelectionFilters**](UtxoSelectionFilters.md) |  | [optional] 
**input_selection** | [**UtxoInputSelection**](UtxoInputSelection.md) |  | [optional] 

## Example

```python
from fireblocks.models.utxo_selection_params import UtxoSelectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoSelectionParams from a JSON string
utxo_selection_params_instance = UtxoSelectionParams.from_json(json)
# print the JSON string representation of the object
print(UtxoSelectionParams.to_json())

# convert the object into a dict
utxo_selection_params_dict = utxo_selection_params_instance.to_dict()
# create an instance of UtxoSelectionParams from a dict
utxo_selection_params_from_dict = UtxoSelectionParams.from_dict(utxo_selection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


