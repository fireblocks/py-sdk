# UtxoInput2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_hash** | **str** | The transaction hash | [optional] 
**index** | **int** | The output index (vout) | [optional] 

## Example

```python
from fireblocks.models.utxo_input2 import UtxoInput2

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoInput2 from a JSON string
utxo_input2_instance = UtxoInput2.from_json(json)
# print the JSON string representation of the object
print(UtxoInput2.to_json())

# convert the object into a dict
utxo_input2_dict = utxo_input2_instance.to_dict()
# create an instance of UtxoInput2 from a dict
utxo_input2_from_dict = UtxoInput2.from_dict(utxo_input2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


