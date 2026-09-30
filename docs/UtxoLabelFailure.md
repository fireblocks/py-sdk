# UtxoLabelFailure

A requested identifier that blocked the label request, with the reason it could not be labelled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | [**UtxoIdentifier**](UtxoIdentifier.md) | The identifier exactly as it was sent in the request. | 
**reason** | **str** | Why the identifier could not be labelled: - &#x60;NOT_FOUND&#x60; — no UTXO for it in this vault and asset. Retrying can work once it is indexed. - &#x60;NOT_LABELLABLE&#x60; — the UTXO exists but can no longer be labelled (spent, or removed; for a transaction ID, every output). Retrying will not help. | 
**utxo_status** | **str** | The UTXO status behind the reason, when one explains it. With &#x60;NOT_FOUND&#x60;, &#x60;REMOVED&#x60; means the UTXO was removed within the last hour and may still reappear; if it does not, the same request returns &#x60;NOT_LABELLABLE&#x60; after about an hour. | [optional] 

## Example

```python
from fireblocks.models.utxo_label_failure import UtxoLabelFailure

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoLabelFailure from a JSON string
utxo_label_failure_instance = UtxoLabelFailure.from_json(json)
# print the JSON string representation of the object
print(UtxoLabelFailure.to_json())

# convert the object into a dict
utxo_label_failure_dict = utxo_label_failure_instance.to_dict()
# create an instance of UtxoLabelFailure from a dict
utxo_label_failure_from_dict = UtxoLabelFailure.from_dict(utxo_label_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


