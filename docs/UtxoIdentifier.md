# UtxoIdentifier

Identifies a UTXO by either a Fireblocks transaction ID (targets all outputs of that transaction) or a specific on-chain UTXO (txHash + index). Exactly one of these two forms must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** | Fireblocks transaction ID | [optional] 
**tx_hash** | **str** | On-chain transaction hash | [optional] 
**index** | **int** | Output index (vout) | [optional] 

## Example

```python
from fireblocks.models.utxo_identifier import UtxoIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoIdentifier from a JSON string
utxo_identifier_instance = UtxoIdentifier.from_json(json)
# print the JSON string representation of the object
print(UtxoIdentifier.to_json())

# convert the object into a dict
utxo_identifier_dict = utxo_identifier_instance.to_dict()
# create an instance of UtxoIdentifier from a dict
utxo_identifier_from_dict = UtxoIdentifier.from_dict(utxo_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


