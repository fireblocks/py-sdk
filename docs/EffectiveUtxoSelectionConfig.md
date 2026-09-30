# EffectiveUtxoSelectionConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | [**UtxoSelectionStrategyEnum**](UtxoSelectionStrategyEnum.md) |  | 
**source** | [**UtxoSelectionConfigSourceEnum**](UtxoSelectionConfigSourceEnum.md) |  | 

## Example

```python
from fireblocks.models.effective_utxo_selection_config import EffectiveUtxoSelectionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EffectiveUtxoSelectionConfig from a JSON string
effective_utxo_selection_config_instance = EffectiveUtxoSelectionConfig.from_json(json)
# print the JSON string representation of the object
print(EffectiveUtxoSelectionConfig.to_json())

# convert the object into a dict
effective_utxo_selection_config_dict = effective_utxo_selection_config_instance.to_dict()
# create an instance of EffectiveUtxoSelectionConfig from a dict
effective_utxo_selection_config_from_dict = EffectiveUtxoSelectionConfig.from_dict(effective_utxo_selection_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


