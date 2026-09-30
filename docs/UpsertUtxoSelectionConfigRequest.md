# UpsertUtxoSelectionConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | [**UtxoSelectionStrategyEnum**](UtxoSelectionStrategyEnum.md) |  | 

## Example

```python
from fireblocks.models.upsert_utxo_selection_config_request import UpsertUtxoSelectionConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertUtxoSelectionConfigRequest from a JSON string
upsert_utxo_selection_config_request_instance = UpsertUtxoSelectionConfigRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertUtxoSelectionConfigRequest.to_json())

# convert the object into a dict
upsert_utxo_selection_config_request_dict = upsert_utxo_selection_config_request_instance.to_dict()
# create an instance of UpsertUtxoSelectionConfigRequest from a dict
upsert_utxo_selection_config_request_from_dict = UpsertUtxoSelectionConfigRequest.from_dict(upsert_utxo_selection_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


