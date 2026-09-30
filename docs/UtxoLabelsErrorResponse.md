# UtxoLabelsErrorResponse

Returned when a label request is rejected. The request is all-or-nothing, so no UTXO was labelled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Summary of the rejection. When &#x60;failures&#x60; is present, it names the identifiers that blocked the request. | 
**failures** | [**List[UtxoLabelFailure]**](UtxoLabelFailure.md) | Every identifier that blocked the request, each with its own reason. Identifiers not listed were valid; resend them without the failed ones. Absent when the request itself was invalid (e.g. a malformed label). | [optional] 

## Example

```python
from fireblocks.models.utxo_labels_error_response import UtxoLabelsErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoLabelsErrorResponse from a JSON string
utxo_labels_error_response_instance = UtxoLabelsErrorResponse.from_json(json)
# print the JSON string representation of the object
print(UtxoLabelsErrorResponse.to_json())

# convert the object into a dict
utxo_labels_error_response_dict = utxo_labels_error_response_instance.to_dict()
# create an instance of UtxoLabelsErrorResponse from a dict
utxo_labels_error_response_from_dict = UtxoLabelsErrorResponse.from_dict(utxo_labels_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


