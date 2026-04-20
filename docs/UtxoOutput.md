# UtxoOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**UtxoInput2**](UtxoInput2.md) |  | 
**utxo_id** | **str** | The unique UTXO identifier | 
**address** | **str** | The address holding this UTXO | 
**amount** | **str** | The UTXO amount in the asset&#39;s native unit | 
**confirmations** | **int** | Number of confirmations | [optional] 
**status** | **str** | The UTXO status | 
**is_change** | **bool** | Whether this is a change output | [optional] 
**is_coinbase** | **bool** | Whether this is a coinbase output | [optional] 
**fb_tx_id** | **str** | The Fireblocks transaction ID that created this UTXO | [optional] 
**created_by_hash** | **str** | The on-chain block hash where this UTXO was created | [optional] 
**spent_by_fb_tx_id** | **List[str]** | Fireblocks transaction IDs that selected/spent this UTXO | [optional] 
**created_by_height** | **int** | The block height at which this UTXO was created | [optional] 
**created_at** | **datetime** | The timestamp when this UTXO was created | [optional] 
**updated_at** | **datetime** | The timestamp when this UTXO was last updated | [optional] 
**labels** | **List[str]** | Labels attached to this UTXO | [optional] 

## Example

```python
from fireblocks.models.utxo_output import UtxoOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoOutput from a JSON string
utxo_output_instance = UtxoOutput.from_json(json)
# print the JSON string representation of the object
print(UtxoOutput.to_json())

# convert the object into a dict
utxo_output_dict = utxo_output_instance.to_dict()
# create an instance of UtxoOutput from a dict
utxo_output_from_dict = UtxoOutput.from_dict(utxo_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


