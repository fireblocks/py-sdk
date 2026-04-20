# AttachDetachUtxoLabelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**utxo_identifiers** | [**List[UtxoIdentifier]**](UtxoIdentifier.md) | List of UTXO identifiers to apply label changes to | 
**labels_to_attach** | **List[str]** | Labels to attach to the specified UTXOs. At least one of labelsToAttach or labelsToDetach must be provided. | [optional] 
**labels_to_detach** | **List[str]** | Labels to detach from the specified UTXOs. At least one of labelsToAttach or labelsToDetach must be provided. | [optional] 

## Example

```python
from fireblocks.models.attach_detach_utxo_labels_request import AttachDetachUtxoLabelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachDetachUtxoLabelsRequest from a JSON string
attach_detach_utxo_labels_request_instance = AttachDetachUtxoLabelsRequest.from_json(json)
# print the JSON string representation of the object
print(AttachDetachUtxoLabelsRequest.to_json())

# convert the object into a dict
attach_detach_utxo_labels_request_dict = attach_detach_utxo_labels_request_instance.to_dict()
# create an instance of AttachDetachUtxoLabelsRequest from a dict
attach_detach_utxo_labels_request_from_dict = AttachDetachUtxoLabelsRequest.from_dict(attach_detach_utxo_labels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


