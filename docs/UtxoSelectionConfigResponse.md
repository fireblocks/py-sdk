# UtxoSelectionConfigResponse

`effective` is always present. `configured` is omitted when no row is stored at the requested scope (the server does not emit `\"configured\": null`). PUT responses always include `configured`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured** | [**UtxoSelectionConfigEntry**](UtxoSelectionConfigEntry.md) |  | [optional] 
**effective** | [**EffectiveUtxoSelectionConfig**](EffectiveUtxoSelectionConfig.md) |  | 

## Example

```python
from fireblocks.models.utxo_selection_config_response import UtxoSelectionConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoSelectionConfigResponse from a JSON string
utxo_selection_config_response_instance = UtxoSelectionConfigResponse.from_json(json)
# print the JSON string representation of the object
print(UtxoSelectionConfigResponse.to_json())

# convert the object into a dict
utxo_selection_config_response_dict = utxo_selection_config_response_instance.to_dict()
# create an instance of UtxoSelectionConfigResponse from a dict
utxo_selection_config_response_from_dict = UtxoSelectionConfigResponse.from_dict(utxo_selection_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


