# SetLayerZeroPeersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The id of the vault account that will be used to inititate transactions ot set peers | 
**source_adapter_token_link_id** | **str** | &#x60;token_link&#x60; ID of the source adapter contract | 
**destination_adapter_token_link_ids** | **List[str]** | Array of &#x60;token_link&#x60; IDs for destination adapter contracts | 
**bidirectional** | **bool** | If true, also sets peers from destination(s) back to source | 

## Example

```python
from fireblocks.models.set_layer_zero_peers_request import SetLayerZeroPeersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetLayerZeroPeersRequest from a JSON string
set_layer_zero_peers_request_instance = SetLayerZeroPeersRequest.from_json(json)
# print the JSON string representation of the object
print(SetLayerZeroPeersRequest.to_json())

# convert the object into a dict
set_layer_zero_peers_request_dict = set_layer_zero_peers_request_instance.to_dict()
# create an instance of SetLayerZeroPeersRequest from a dict
set_layer_zero_peers_request_from_dict = SetLayerZeroPeersRequest.from_dict(set_layer_zero_peers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


