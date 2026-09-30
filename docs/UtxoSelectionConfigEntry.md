# UtxoSelectionConfigEntry

Config row stored at exactly the requested scope. Omitted from the parent object when none exists; the server does not emit JSON `null`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | [**UtxoSelectionStrategyEnum**](UtxoSelectionStrategyEnum.md) |  | 
**updated_at** | **datetime** | Time at which this configured row was last updated. | 

## Example

```python
from fireblocks.models.utxo_selection_config_entry import UtxoSelectionConfigEntry

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoSelectionConfigEntry from a JSON string
utxo_selection_config_entry_instance = UtxoSelectionConfigEntry.from_json(json)
# print the JSON string representation of the object
print(UtxoSelectionConfigEntry.to_json())

# convert the object into a dict
utxo_selection_config_entry_dict = utxo_selection_config_entry_instance.to_dict()
# create an instance of UtxoSelectionConfigEntry from a dict
utxo_selection_config_entry_from_dict = UtxoSelectionConfigEntry.from_dict(utxo_selection_config_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


