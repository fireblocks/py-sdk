# SetLayerZeroPeersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txn_ids** | **List[str]** | Array of fireblocks transaction IDs, each corresponding to an on-chain transaction to set peers | 

## Example

```python
from fireblocks.models.set_layer_zero_peers_response import SetLayerZeroPeersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetLayerZeroPeersResponse from a JSON string
set_layer_zero_peers_response_instance = SetLayerZeroPeersResponse.from_json(json)
# print the JSON string representation of the object
print(SetLayerZeroPeersResponse.to_json())

# convert the object into a dict
set_layer_zero_peers_response_dict = set_layer_zero_peers_response_instance.to_dict()
# create an instance of SetLayerZeroPeersResponse from a dict
set_layer_zero_peers_response_from_dict = SetLayerZeroPeersResponse.from_dict(set_layer_zero_peers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


