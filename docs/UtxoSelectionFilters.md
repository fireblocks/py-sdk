# UtxoSelectionFilters

Narrow the UTXO candidate pool. All specified filters are AND-ed together. This feature is currently in beta and might be subject to changes. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_all_labels** | **List[str]** | Only include UTXOs that have ALL of these labels. | [optional] 
**include_any_labels** | **List[str]** | Only include UTXOs that have at least one of these labels. | [optional] 
**exclude_any_labels** | **List[str]** | Exclude UTXOs that have any of these labels. | [optional] 
**address** | **str** | Only include UTXOs from this specific address. | [optional] 
**min_amount** | **str** | Minimum UTXO amount in the asset&#39;s base unit (e.g., BTC). | [optional] 
**max_amount** | **str** | Maximum UTXO amount in the asset&#39;s base unit (e.g., BTC). | [optional] 
**use_change** | **bool** | Set to false to exclude change UTXOs. Default is true. | [optional] 
**use_coinbase** | **bool** | Set to false to exclude coinbase UTXOs. Default is true. | [optional] 

## Example

```python
from fireblocks.models.utxo_selection_filters import UtxoSelectionFilters

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoSelectionFilters from a JSON string
utxo_selection_filters_instance = UtxoSelectionFilters.from_json(json)
# print the JSON string representation of the object
print(UtxoSelectionFilters.to_json())

# convert the object into a dict
utxo_selection_filters_dict = utxo_selection_filters_instance.to_dict()
# create an instance of UtxoSelectionFilters from a dict
utxo_selection_filters_from_dict = UtxoSelectionFilters.from_dict(utxo_selection_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


