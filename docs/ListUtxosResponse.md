# ListUtxosResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UtxoOutput]**](UtxoOutput.md) | List of UTXOs | 
**next** | **str** | Cursor to the next page | [optional] 

## Example

```python
from fireblocks.models.list_utxos_response import ListUtxosResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUtxosResponse from a JSON string
list_utxos_response_instance = ListUtxosResponse.from_json(json)
# print the JSON string representation of the object
print(ListUtxosResponse.to_json())

# convert the object into a dict
list_utxos_response_dict = list_utxos_response_instance.to_dict()
# create an instance of ListUtxosResponse from a dict
list_utxos_response_from_dict = ListUtxosResponse.from_dict(list_utxos_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


