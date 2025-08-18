# RemoveLayerZeroPeersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txn_ids** | **List[str]** | Array of fireblocks transaction IDs, each corresponding to an on-chain transaction to set peers | 

## Example

```python
from fireblocks.models.remove_layer_zero_peers_response import RemoveLayerZeroPeersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveLayerZeroPeersResponse from a JSON string
remove_layer_zero_peers_response_instance = RemoveLayerZeroPeersResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveLayerZeroPeersResponse.to_json())

# convert the object into a dict
remove_layer_zero_peers_response_dict = remove_layer_zero_peers_response_instance.to_dict()
# create an instance of RemoveLayerZeroPeersResponse from a dict
remove_layer_zero_peers_response_from_dict = RemoveLayerZeroPeersResponse.from_dict(remove_layer_zero_peers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


