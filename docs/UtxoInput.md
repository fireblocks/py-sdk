# UtxoInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_hash** | **str** |  | 
**vout** | **int** |  | 

## Example

```python
from fireblocks.models.utxo_input import UtxoInput

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoInput from a JSON string
utxo_input_instance = UtxoInput.from_json(json)
# print the JSON string representation of the object
print(UtxoInput.to_json())

# convert the object into a dict
utxo_input_dict = utxo_input_instance.to_dict()
# create an instance of UtxoInput from a dict
utxo_input_from_dict = UtxoInput.from_dict(utxo_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


