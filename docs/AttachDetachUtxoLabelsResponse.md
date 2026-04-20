# AttachDetachUtxoLabelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**utxos** | [**List[UtxoOutput]**](UtxoOutput.md) | Modified UTXOs with updated labels | [optional] 

## Example

```python
from fireblocks.models.attach_detach_utxo_labels_response import AttachDetachUtxoLabelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachDetachUtxoLabelsResponse from a JSON string
attach_detach_utxo_labels_response_instance = AttachDetachUtxoLabelsResponse.from_json(json)
# print the JSON string representation of the object
print(AttachDetachUtxoLabelsResponse.to_json())

# convert the object into a dict
attach_detach_utxo_labels_response_dict = attach_detach_utxo_labels_response_instance.to_dict()
# create an instance of AttachDetachUtxoLabelsResponse from a dict
attach_detach_utxo_labels_response_from_dict = AttachDetachUtxoLabelsResponse.from_dict(attach_detach_utxo_labels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


